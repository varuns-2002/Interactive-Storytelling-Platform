document.getElementById('submit-action').addEventListener('click', function() {
    const userInput = document.getElementById('input-action').value;
    fetch('/process_input', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('world-state-content').innerText = data.worldState;
        document.getElementById('narration-content').innerText = data.narration;
        document.getElementById('predicted-outcomes-content').innerText = data.predictedOutcomes;
        document.getElementById('predicted-narration-content').innerText = data.predictedNarration;
    });
});
