# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_render():
    """
    Renders a simple 'Hello, Render!' message when the root URL is accessed.
    """
    return "Hello, Render!"

if __name__ == '__main__':
    # This block is for local development only.
    # Render.com will use Gunicorn to run the app in production.
    app.run(debug=True, host='0.0.0.0', port=5000)
