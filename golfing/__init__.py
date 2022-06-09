from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from datetime import datetime


app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bubvrggvtgdkak:0d9aa47763aeb830234c8b737b2533ea56b5129ed262e8e11b1c5b8cc872406b@ec2-34-198-186-145.compute-1.amazonaws.com:5432/dfchtt25oviqg7'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from golfing import routes

