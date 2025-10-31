from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import logging
from typing import Tuple

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

@app.route('/execute', methods=['POST'])
def execute_code() -> Tuple[str, str]:
    """Executes the provided Python code and returns the output or error message.

    Args:
        code (str): The Python code to execute.

    Returns:
        Tuple[str, str]: A tuple containing the output of the code execution
                         and any error message generated during execution.
    """
    data = request.get_json()
    code = data.get('code', '')

    if not code:
        return jsonify({"output": "", "error_message": "No code provided"}), 400

    try:
        result = subprocess.run(
            ['python3', '-c', code],
            capture_output=True,
            text=True,
            check=True
        )
        return jsonify({"output": result.stdout, "error_message": None}), 200
    except subprocess.CalledProcessError as e:
        logger.error(f"Execution error: {e.stderr.strip()}")
        return jsonify({"output": "", "error_message": e.stderr.strip()}), 500


if __name__ == '__main__':
    app.run(debug=True)