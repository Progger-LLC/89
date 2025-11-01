from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os
import logging
from typing import Tuple

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set up logging
logging.basicConfig(level=logging.INFO)

def execute_code(code: str) -> Tuple[str, str]:
    """Execute the given Python code and return the output and error message.

    Args:
        code (str): The Python code to execute.

    Returns:
        Tuple[str, str]: A tuple containing the output of the code execution and any error message.
    """
    try:
        # Use subprocess to execute the code in a secure way
        result = subprocess.run(['python3', '-c', code], capture_output=True, text=True)
        output = result.stdout.strip()
        error_message = result.stderr.strip()
        return output, error_message
    except Exception as e:
        logging.error(f"Execution error: {str(e)}")
        return "", f"Execution failed: {str(e)}"

@app.route('/execute', methods=['POST'])
def run_code():
    """Handle the execution of Python code sent via a POST request.

    Returns:
        JSON response with output or error message.
    """
    data = request.get_json()
    
    if not data or 'code' not in data:
        return jsonify({"error": {"code": "BAD_REQUEST", "message": "No code provided"}}), 400
    
    code = data['code']
    output, error_message = execute_code(code)
    
    if error_message:
        return jsonify({"output": "", "error_message": error_message}), 400
    
    return jsonify({"output": output, "error_message": None}), 200

if __name__ == '__main__':
    app.run(debug=True)