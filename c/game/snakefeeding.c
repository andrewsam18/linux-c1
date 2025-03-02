#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <termios.h>
#include <fcntl.h>

int i, j, height = 20, width = 20;
int gameover, score;
int x, y, eggx, eggy, flag;

// Function to generate the egg within the boundary
void setup()
{
    gameover = 0;
    // Stores height and width
    x = height / 2;
    y = width / 2;

    do
    {
        eggx = rand() % 20;
    } while (eggx == 0);

    do
    {
        eggy = rand() % 20;
    } while (eggy == 0);

    score = 0;
}

// Function to draw the boundaries
void draw()
{
    system("clear");
    for (i = 0; i < height; i++)
    {
        for (j = 0; j < width; j++)
        {
            if (i == 0 || i == width - 1 || j == 0 || j == height - 1)
            {
                printf("#");
            }
            else
            {
                if (i == x && j == y)
                    printf("0");
                else if (i == eggx && j == eggy)
                    printf("*");
                else
                    printf(" ");
            }
        }
        printf("\n");
    }

    // Print the score after the game ends
    printf("score = %d\n", score);
    printf("press X to quit the game\n");
}

// Function to take the input
int kbhit(void)
{
    struct termios oldt, newt;
    int ch;
    int oldf;

    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;
    newt.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    oldf = fcntl(STDIN_FILENO, F_GETFL, 0);
    fcntl(STDIN_FILENO, F_SETFL, oldf | O_NONBLOCK);

    ch = getchar();

    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
    fcntl(STDIN_FILENO, F_SETFL, oldf);

    if (ch != EOF)
    {
        ungetc(ch, stdin);
        return 1;
    }

    return 0;
}

char getch()
{
    char buf = 0;
    struct termios old = {0};
    if (tcgetattr(0, &old) < 0)
        perror("tcsetattr()");
    old.c_lflag &= ~ICANON;
    old.c_lflag &= ~ECHO;
    old.c_cc[VMIN] = 1;
    old.c_cc[VTIME] = 0;
    if (tcsetattr(0, TCSANOW, &old) < 0)
        perror("tcsetattr ICANON");
    if (read(0, &buf, 1) < 0)
        perror("read()");
    old.c_lflag |= ICANON;
    old.c_lflag |= ECHO;
    if (tcsetattr(0, TCSADRAIN, &old) < 0)
        perror("tcsetattr ~ICANON");
    return buf;
}

void input()
{
    if (kbhit())
    {
        switch (getch())
        {
        case 'a':
            flag = 1;
            break;
        case 's':
            flag = 2;
            break;
        case 'd':
            flag = 3;
            break;
        case 'w':
            flag = 4;
            break;
        case 'x':
            gameover = 1;
            break;
        }
    }
}

// Function for the logic behind each movement
void logic()
{
    usleep(100000); // sleep for 100ms
    switch (flag)
    {
    case 1:
        y--;
        break;
    case 2:
        x++;
        break;
    case 3:
        y++;
        break;
    case 4:
        x--;
        break;
    default:
        break;
    }

    // If the game is over
    if (x < 0 || x > height || y < 0 || y > width)
        gameover = 1;

    // If snake reaches the egg, then update the score
    if (x == eggx && y == eggy)
    {
        do
        {
            eggx = rand() % 20;
        } while (eggx == 0);

        do
        {
            eggy = rand() % 20;
        } while (eggy == 0);

        score += 10;
    }
}

// Driver Code
int main()
{
    int m, n;
    // Generate boundary
    setup();
    // Until the game is over
    while (!gameover)
    {
        // Function Call
        draw();
        input();
        logic();
    }
    return 0;
}
