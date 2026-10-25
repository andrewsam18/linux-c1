import tkinter
import tkinter.font as tkfont
import math

# Maximum number of characters allowed on the display
MAX_LENGTH = 24

# Layout sizes (pixels)
COL_WIDTH = 92
ROW_HEIGHT = 72
DISPLAY_PADX = 14
DISPLAY_WIDTH = 4 * COL_WIDTH - 2 * DISPLAY_PADX - 4  # usable text width
button_values = [
    ["AC", "DEL", "+/-", "%"],
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    ["0", ".", "√", "+"],
    ["="],
]
right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "DEL", "+/-", "%"]

# Colors: (normal, pressed)
color_black = "#1C1C1C"
color_white = "white"
color_grey_text = "#9a9a9a"
colors_light_gray = ("#D4D4D2", "#F0F0EE")
colors_dark_gray = ("#505050", "#707070")
colors_orange = ("#FF9500", "#FFB340")

# Window setup
window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)
window.configure(bg=color_black)

frame = tkinter.Frame(window, bg=color_black)
frame.pack()
# Equal-width columns, fixed-height rows so the layout never shifts
for c in range(4):
    frame.columnconfigure(c, minsize=COL_WIDTH, uniform="col", weight=1)
for r in range(2, len(button_values) + 2):
    frame.rowconfigure(r, minsize=ROW_HEIGHT, weight=1)
# Small line above the display showing the pending operation, e.g. "12 +"
expr_label = tkinter.Label(
    frame,
    text="",
    font=("Arial", 14),
    background=color_black,
    foreground=color_grey_text,
    anchor="e",
    padx=DISPLAY_PADX,
    width=1,
)
expr_label.grid(row=0, column=0, columnspan=4, sticky="we", pady=(10, 0))

# Main display. It shrinks its font to fit instead of widening the window.
display_font = tkfont.Font(family="Arial", size=40)
label = tkinter.Label(
    frame,
    text="0",
    font=display_font,
    background=color_black,
    foreground=color_white,
    anchor="e",
    padx=DISPLAY_PADX,
    pady=6,
    width=1,
)
label.grid(row=1, column=0, columnspan=4, sticky="we", pady=(0, 8))

# Calculator variables
A = "0"
operator = None
just_calculated = False
# True right after an operator was pressed, before a second operand was typed
fresh_operand = False

ERROR_TEXTS = ("Error", "Cannot divide by 0")


def clear_all():
    global A, operator, just_calculated, fresh_operand
    A = "0"
    operator = None
    just_calculated = False
    fresh_operand = False


def format_number(num):
    if not math.isfinite(num):
        return "Error"
    if num == 0:
        return "0"

    # Integers: prefer the plain form, fall back to scientific if too long
    if num.is_integer():
        plain = str(int(num))
        if len(plain) <= MAX_LENGTH:
            return plain
        return f"{num:.6e}"[:MAX_LENGTH]

    # Non-integers: use the shortest round-trippable representation.
    # repr() gives things like "0.5" and "1.25"; strip a trailing ".0".
    plain = repr(float(num))
    if plain.endswith(".0"):
        plain = plain[:-2]
    if len(plain) <= MAX_LENGTH:
        return plain

    # Too long -> scientific notation
    return f"{num:.6e}"[:MAX_LENGTH]


def set_display(text):
    text = text[:MAX_LENGTH]
    # Pick the largest font size whose text fits the display width
    for size in (40, 34, 28, 20, 16, 14):
        display_font.configure(size=size)
        if display_font.measure(text) <= DISPLAY_WIDTH:
            break
    label.config(text=text)


def update_expression():
    expr_label.config(text=f"{A} {operator}" if operator else "")


def current_number():
    """Parse the main display, returning None if it isn't a valid number."""
    text = label["text"]
    if text in ERROR_TEXTS:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def enter_digit(value):
    global just_calculated, fresh_operand
    current = label["text"]
    if current in ERROR_TEXTS:
        clear_all()
        set_display(value)
        return
    if just_calculated:
        # Start a brand-new number after "="
        set_display(value)
        just_calculated = False
        fresh_operand = False
        return
    if fresh_operand:
        # First digit after an operator replaces the placeholder 0
        set_display(value)
        fresh_operand = False
        return
    if current == "0":
        set_display(value)
    elif len(current) < MAX_LENGTH:
        set_display(current + value)


def enter_decimal():
    global just_calculated, fresh_operand
    current = label["text"]
    if current in ERROR_TEXTS or just_calculated or fresh_operand:
        set_display("0.")
        just_calculated = False
        fresh_operand = False
        return
    if "." not in current and len(current) < MAX_LENGTH:
        set_display(current + ".")


def delete_last():
    global just_calculated, fresh_operand
    current = label["text"]
    if current in ERROR_TEXTS:
        clear_all()
        set_display("0")
        return
    # If the display is a computed result, DEL clears it
    if just_calculated or fresh_operand:
        just_calculated = False
        fresh_operand = False
        set_display("0")
        return
    if len(current) <= 1:
        set_display("0")
        return
    trimmed = current[:-1]
    # Never leave a bare "-" or "-." behind
    if trimmed in ("-", "-.", ""):
        trimmed = "0"
    set_display(trimmed)


def calculate():
    global A, operator, just_calculated, fresh_operand
    if operator is None:
        return
    numA = float(A)
    text_b = label["text"]
    if text_b in ERROR_TEXTS:
        return
    try:
        numB = float(text_b)
    except ValueError:
        return

    try:
        if operator == "+":
            result = numA + numB
        elif operator == "-":
            result = numA - numB
        elif operator == "×":
            result = numA * numB
        elif operator == "÷":
            if numB == 0:
                clear_all()
                set_display("Cannot divide by 0")
                return
            result = numA / numB
        else:
            return
    except (ValueError, OverflowError):
        clear_all()
        set_display("Error")
        return

    A = "0"
    operator = None
    just_calculated = True
    fresh_operand = False
    set_display(format_number(result))
    update_expression()


def handle_button(value):
    global A, operator, just_calculated, fresh_operand

    if value == "":
        return

    current = label["text"]

    if value == "AC":
        clear_all()
        set_display("0")
        return

    if value == "DEL":
        delete_last()
        return

    # Any other button pressed while in an error state resets first
    if current in ERROR_TEXTS:
        clear_all()
        set_display("0")
        current = "0"

    # ---- Unary operations ----
    if value == "√":
        num = current_number()
        if num is None:
            return
        if num < 0:
            clear_all()
            set_display("Error")
            return
        set_display(format_number(math.sqrt(num)))
        just_calculated = True
        fresh_operand = False
        return

    if value == "+/-":
        num = current_number()
        if num is None:
            return
        set_display(format_number(-num))
        # Keep just_calculated/fresh_operand as-is: sign flip edits the value
        return

    if value == "%":
        num = current_number()
        if num is None:
            return
        if operator is not None and not fresh_operand:
            # iOS behavior: A + B%  =>  A + (A * B / 100)
            numA = float(A)
            new_value = numA * num / 100
        else:
            new_value = num / 100
        set_display(format_number(new_value))
        fresh_operand = False
        return

    # ---- Binary operators ----
    if value in ("+", "-", "×", "÷"):
        if operator is not None and not fresh_operand:
            # Commit the pending operation first
            calculate()
            if label["text"] in ERROR_TEXTS:
                return
            current = label["text"]
        # If an operator was pressed twice in a row, just swap it
        A = current
        operator = value
        just_calculated = False
        fresh_operand = True
        update_expression()
        return

    # ---- Equals ----
    if value == "=":
        calculate()
        return

    # ---- Decimal point ----
    if value == ".":
        enter_decimal()
        return

    # ---- Digits ----
    if value in "0123456789":
        enter_digit(value)
        return


def button_clicked(value):
    handle_button(value)


# Buttons are Labels with click bindings: unlike tkinter.Button, Label
# colors are honored on every platform (including macOS).
def make_button(value, row, column, columnspan=1):
    if value in top_symbols:
        normal, pressed = colors_light_gray
        fg = color_black
    elif value in right_symbols:
        normal, pressed = colors_orange
        fg = color_white
    else:
        normal, pressed = colors_dark_gray
        fg = color_white
    btn = tkinter.Label(
        frame,
        text=value,
        font=("Arial", 22),
        background=normal,
        foreground=fg,
        cursor="hand2",
    )
    btn.grid(
        row=row + 2,
        column=column,
        columnspan=columnspan,
        sticky="nsew",
        padx=1,
        pady=1,
    )

    def on_press(event):
        btn.config(background=pressed)

    def on_release(event):
        btn.config(background=normal)
        # Only trigger if the pointer is still over the button
        if 0 <= event.x <= btn.winfo_width() and 0 <= event.y <= btn.winfo_height():
            button_clicked(value)

    btn.bind("<ButtonPress-1>", on_press)
    btn.bind("<ButtonRelease-1>", on_release)


# Create buttons
for row, row_value in enumerate(button_values):
    for column, value in enumerate(row_value):
        if value == "":
            continue
        span = 4 if value == "=" else 1
        make_button(value, row, column, span)


# Keyboard input
def keyboard_input(event):
    key = event.keysym
    char = event.char
    if char and char in "0123456789":
        button_clicked(char)
    elif char == ".":
        button_clicked(".")
    elif char in ("+", "-"):
        button_clicked(char)
    elif char in ("*", "x", "X"):
        button_clicked("×")
    elif char == "/":
        button_clicked("÷")
    elif key in ("Return", "KP_Enter") or char == "=":
        button_clicked("=")
    elif key == "BackSpace":
        button_clicked("DEL")
    elif key in ("Escape", "Delete"):
        button_clicked("AC")
    elif char == "%":
        button_clicked("%")
    return "break"


window.bind("<Key>", keyboard_input)


# Initial display
set_display("0")
update_expression()

# Center window
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

window.geometry(f"+{x}+{y}")

# Run calculator
window.mainloop()