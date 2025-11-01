document.getElementById('runButton').addEventListener('click', async () => {
    const code = document.getElementById('codeInput').value;
    
    const response = await fetch('/execute', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code }),
    });
    
    const result = await response.json();
    
    const outputDiv = document.getElementById('output');
    if (response.ok) {
        outputDiv.innerHTML = `<pre>${result.output}</pre>`;
    } else {
        outputDiv.innerHTML = `<pre>Error: ${result.error_message}</pre>`;
    }
});