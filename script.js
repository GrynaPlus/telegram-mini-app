document.getElementById('start-game').addEventListener('click', function() {
    document.getElementById('game-container').style.display = 'block';
    this.style.display = 'none';

    startGame();
});

function startGame() {
    const questions = [
        { question: 'Ile to 2 + 2?', answer: '4' },
        { question: 'Ile to 3 + 5?', answer: '8' },
        { question: 'Ile to 5 + 5?', answer: '10' },
        // Możesz dodać więcej pytań...
    ];

    let currentQuestion = 0;
    const questionContainer = document.getElementById('question-container');

    function askQuestion() {
        if (currentQuestion < questions.length) {
            const q = questions[currentQuestion];
            questionContainer.innerHTML = `
                <p>${q.question}</p>
                <input type="text" id="answer">
                <button onclick="checkAnswer('${q.answer}')">Odpowiedz</button>
            `;
        } else {
            questionContainer.innerHTML = `<p>Wszystkie pytania zostały rozwiązane! Gratulacje!</p>`;
        }
    }

    askQuestion();
}

function checkAnswer(correctAnswer) {
    const userAnswer = document.getElementById('answer').value;
    if (userAnswer === correctAnswer) {
        alert('Poprawna odpowiedź!');
        currentQuestion++;
        startGame();
    } else {
        alert('Zła odpowiedź! Odpowiedz ponownie.');
    }
}
