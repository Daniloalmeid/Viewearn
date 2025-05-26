from flask import Flask, render_template, request, redirect, url_for
from database import db
from models import User, Video, View
from schemas import UserSchema, VideoSchema, ViewSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///viewearn.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/videos')
def videos():
    videos = Video.query.all()
    return render_template('video.html', videos=videos)

@app.route('/dashboard/user')
def dashboard_user():
    # Lógica para exibir o dashboard do usuário
    return render_template('dashboard-user.html')

@app.route('/dashboard/creator')
def dashboard_creator():
    # Lógica para exibir o dashboard do criador de conteúdo
    return render_template('dashboard-creator.html')

@app.route('/register/creator', methods=['GET', 'POST'])
def register_creator():
    if request.method == 'POST':
        # Lógica para registrar um novo criador de conteúdo
        pass
    return render_template('register-creator.html')

if __name__ == '__main__':
    app.run(debug=True)
