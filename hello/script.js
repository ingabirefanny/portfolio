let gameBoard = document.getElementById('game-board');
let cells = document.querySelectorAll('.cell');
let currentPlayer = 'X';
let gameWon = false;

cells.forEach((cell) => {
    cell.addEventListener('click', (e) => {
        if (!gameWon && cell.textContent === '') {
            cell.textContent = currentPlayer;
            checkForWin();
            currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
        }
    });
});

function checkForWin() {
    let winningCombinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ];

    winningCombinations.forEach((combination) => {
        let cell1 = cells[combination[0]].textContent;
        let cell2 = cells[combination[1]].textContent;
        let cell3 = cells[combination[2]].textContent;

        if (cell1 === cell2 && cell2 === cell3 && cell1 !== '') {
            gameWon = true;
            alert(`Player ${cell1} wins`);
        }
    });
}

gameBoard.addEventListener('click', (e) => {
    if (gameWon) {
        alert('Game over!');
        gameWon = false;
        currentPlayer = 'X';
        cells.forEach((cell) => {
            cell.textContent = '';
        });
    }
});
