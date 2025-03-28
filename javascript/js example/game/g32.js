let playerText = document.getElementById('playerText');
let restartBtn = document.getElementById('restartBtn');
let boxes = Array.from(document.getElementsByClassName('box'));

let winnerIndicator = getComputedStyle(document.body).getPropertyValue('--winning-blocks');

const O_TEXT = "O";
const X_TEXT = "X";
let currentPlayer = X_TEXT;
let spaces = Array(9).fill(null);
let gameActive = true; // Controls game flow

const startGame = () => {
    boxes.forEach(box => box.addEventListener('click', boxClicked));
};

function boxClicked(e) {
    const id = parseInt(e.target.id);

    if (!spaces[id] && gameActive && currentPlayer === X_TEXT) {
        // Human (X) move
        spaces[id] = currentPlayer;
        e.target.innerText = currentPlayer;

        if (checkGameStatus()) return;

        currentPlayer = O_TEXT;
        setTimeout(autoPlayO, 500); // Delay for "O" to play automatically
    }
}

function autoPlayO() {
    if (!gameActive) return; // Stop if game is over

    let availableSpaces = spaces.map((val, idx) => (val === null ? idx : null)).filter(v => v !== null);
    if (availableSpaces.length === 0) return;

    let randomIndex = availableSpaces[Math.floor(Math.random() * availableSpaces.length)];
    
    spaces[randomIndex] = O_TEXT;
    boxes[randomIndex].innerText = O_TEXT;

    if (checkGameStatus()) return;

    currentPlayer = X_TEXT; // Give control back to human player
}

function checkGameStatus() {
    let winningBlocks = playerHasWon();
    if (winningBlocks) {
        playerText.innerText = `${currentPlayer} has won! 🎉`;
        winningBlocks.forEach(index => (boxes[index].style.backgroundColor = winnerIndicator));
        gameActive = false;
        return true;
    }

    if (!spaces.includes(null)) {
        playerText.innerText = "It's a draw! 🤝";
        gameActive = false;
        return true;
    }

    return false;
}

const winningCombos = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], 
    [0, 3, 6], [1, 4, 7], [2, 5, 8], 
    [0, 4, 8], [2, 4, 6]
];

function playerHasWon() {
    for (const condition of winningCombos) {
        let [a, b, c] = condition;
        if (spaces[a] && spaces[a] === spaces[b] && spaces[a] === spaces[c]) {
            return condition;
        }
    }
    return null;
}

restartBtn.addEventListener('click', restart);

function restart() {
    spaces.fill(null);
    boxes.forEach(box => {
        box.innerText = '';
        box.style.backgroundColor = '';
    });

    playerText.innerText = 'Tic-Tac-Toe';
    currentPlayer = X_TEXT;
    gameActive = true;
}

startGame();
