document.getElementById('runButton').addEventListener('click', async function() {
    const code = document.getElementById('codeInput').value;
    const response = await fetch('/execute', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code })
    });

    const result = await response.json();
    const outputDisplay = document.getElementById('outputDisplay');
    if (response.ok) {
        outputDisplay.textContent = `Output:\n${result.output}`;
    } else {
        outputDisplay.textContent = `Error:\n${result.error_message}`;
    }
});