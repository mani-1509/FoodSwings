from flask import Blueprint , render_template , request

views = Blueprint('views' , __name__)

@views.route('/')

def home():
    return render_template('index.html')

@views.route('/login')
def login():
    return render_template('login.html')