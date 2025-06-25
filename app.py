from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Business, Service, Client
from forms import AdminLoginForm, BusinessForm, ServiceForm
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'replace_with_a_random_secret'

db.init_app(app)

# Fixed: @app.before_first_request is deprecated in Flask 2.2+
# Use app context instead
with app.app_context():
    db.create_all()


# Remember to REMOVE or COMMENT OUT this route after running ONCE!


@app.route('/', methods=['GET'])
def home():
    # List all businesses for demo—click to chat
    studios = Business.query.all()
    return render_template('home.html', studios=studios)

# ---- ADMIN AREA ----
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            session['user_id'] = user.id
            return redirect(url_for('admin_dashboard'))
        else:
            flash("Invalid login.")
    return render_template('admin_login.html', form=form)

@app.route('/admin/logout')
def admin_logout():
    session.pop('user_id', None)
    flash("Logged out!")
    return redirect(url_for('admin_login'))

@app.route('/admin/dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    if 'user_id' not in session:
        return redirect(url_for('admin_login'))
    user = User.query.get(session['user_id'])
    
    # Fixed: Added safety check for user existence
    if not user:
        session.pop('user_id', None)
        return redirect(url_for('admin_login'))
    
    biz = user.businesses[0] if user.businesses else None

    if request.method == "POST" and biz:
        # Update business info
        biz.name = request.form.get("name")
        biz.address = request.form.get("address")
        biz.phone = request.form.get("phone")
        biz.whatsapp = request.form.get("whatsapp")
        biz.hours = request.form.get("hours")
        biz.welcome_message = request.form.get("welcome_message")
        db.session.commit()
        flash("Info updated!")

    return render_template('admin_dashboard.html', business=biz, user=user)

@app.route('/admin/services/add', methods=['GET', 'POST'])
def add_service():
    if 'user_id' not in session:
        return redirect(url_for('admin_login'))
    user = User.query.get(session['user_id'])
    
    # Fixed: Added safety checks
    if not user or not user.businesses:
        flash("No business found for this user.")
        return redirect(url_for('admin_dashboard'))
    
    biz = user.businesses[0]
    if request.method == "POST":
        s = Service(
            business_id=biz.id,
            name=request.form['name'],
            price=request.form['price'],
            duration=request.form['duration'])
        db.session.add(s)
        db.session.commit()
        flash("Service added!")
        return redirect(url_for('admin_dashboard'))
    return render_template('add_service.html')

# ---- CLIENT/CHAT AREA ----
@app.route('/chat/<int:biz_id>', methods=['GET', 'POST'])
def chat(biz_id):
    biz = Business.query.get_or_404(biz_id)
    if request.method == "POST":
        # Simple "client memory": ask for name first time
        client_name = request.form['name']
        client = Client.query.filter_by(business_id=biz_id, name=client_name).first()
        if not client:
            client = Client(
                business_id=biz_id,
                name=client_name,
                last_seen=datetime.utcnow())
            db.session.add(client)
            db.session.commit()
        else:
            client.last_seen = datetime.utcnow()
            db.session.commit()
        # For MVP: simple echo, you can replace this with AI logic
        user_message = request.form['message']
        bot_message = f"{biz.welcome_message or 'Olá!'} {client.name}, como posso ajudar com nossos serviços?"
        return render_template('chat.html', business=biz, client_name=client.name, chat=[("you", user_message), ("bot", bot_message)])
    return render_template('chat.html', business=biz, client_name=None, chat=None)

if __name__ == '__main__':
    app.run(debug=True)
