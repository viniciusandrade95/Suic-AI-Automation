# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# SQLite uses a URI that starts with 'sqlite:///path_to_db_file'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'   # File named app.db in your project folder
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- Models ---

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    businesses = db.relationship('Business', backref='owner', lazy=True)

class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(255), nullable=False)
    whatsapp = db.Column(db.String(30))
    phone = db.Column(db.String(30))
    address = db.Column(db.String(255))
    hours = db.Column(db.String(255))
    welcome_message = db.Column(db.Text)
    bot_persona = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    services = db.relationship('Service', backref='business', lazy=True)
    clients = db.relationship('Client', backref='business', lazy=True)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(50))
    duration = db.Column(db.String(30))

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    name = db.Column(db.String(255))
    contact = db.Column(db.String(255))
    last_seen = db.Column(db.DateTime)
    notes = db.Column(db.Text)

# --- Startup ---

@app.route('/')
def hello_render():
    """
    Renders a simple 'Hello, Render!' message when the root URL is accessed.
    """
    return "Hello, Render!"

if __name__ == '__main__':
    # This block is for local development only.
    # Render.com will use Gunicorn to run the app in production.
    with app.app_context():
        db.create_all()  # This line creates app.db and all tables if not exists
    print("Database created (if not exists). You can now start building features!")
    #app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=5000)
