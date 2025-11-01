document.getElementById('run-button').onclick = function() {
    const code = document.getElementById('code-input').value;
    fetch('/execute', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ code: code })
    })
    .then(response => response.json())
    .then(data => {
        const outputDiv = document.getElementById('output');
        outputDiv.innerHTML = '';
        if (data.error_message) {
            outputDiv.innerHTML = `<span style="color:red;">Error: ${data.error_message}</span>`;
        } else {
            outputDiv.innerHTML = `<span style="color:green;">Output: ${data.output}</span>`;
        }
    })
    .catch(error => console.error('Error:', error));
};