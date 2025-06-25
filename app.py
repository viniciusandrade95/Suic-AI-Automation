# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# SQLite uses a URI that starts with 'sqlite:///path_to_db_file'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'   # File named app.db in your project folder
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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
