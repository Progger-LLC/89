from flask import Flask, request, jsonify, render_template
from typing import Tuple
import traceback
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

def execute_code(code: str) -> Tuple[str, str]:
    """Execute the provided Python code.

    Args:
        code: The Python code to execute.

    Returns:
        A tuple containing:
        - output: The output of the code execution.
        - error_message: Any error message generated during execution.
    """
    output, error_message = "", ""
    try:
        exec_locals = {}
        exec(code, {}, exec_locals)
        output = exec_locals.get('output', '')
    except Exception as e:
        error_message = str(e)
        logging.error("Error executing code: %s", traceback.format_exc())
    return output, error_message

@app.route('/')
def index():
    """Render the main application page."""
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    """Handle code execution requests."""
    data = request.get_json()
    code = data.get('code', '')
    output, error_message = execute_code(code)
    return jsonify({'output': output, 'error_message': error_message})

if __name__ == '__main__':
    app.run(debug=True)