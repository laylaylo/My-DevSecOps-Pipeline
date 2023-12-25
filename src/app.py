"""Module docstring: Description of what this module does."""

import socket
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    """Function docstring: Explain what this function does."""
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except Exception as e:  # Replace Exception with a more specific exception if possible
        return render_template('error.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)