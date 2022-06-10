from datetime import datetime
from xmlrpc.client import DateTime
from golfing import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(256), unique=False, nullable=True)
    last_name = db.Column(db.String(256), unique=False, nullable=True)
    user_email= db.Column(db.String(256), unique=True, nullable=False)
    user_password = db.Column(db.String(256), nullable=False)
    # posts = db.relationship('Post', backref='author', lazy=True)
    # image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    posts = db.relationship("Post", back_populates="user")

    def __repr__(self):
        return f"User('{self.last_name}', '{self.user_email}', '{self.image_file}')"


class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating_score = db.Column(db.Integer, nullable=False)
    course_difficulty = db.Column(db.Integer, nullable=False)
    course_location = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Text, nullable=False)

class Course_rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", back_populates="posts")
    content = db.Column(db.Text, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)
#     posts = db.relationship('Post', backref='author', lazy=True)

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __repr__(self):
#         return f"Post('{self.title}', '{self.date_posted}')"


# class Gcourse(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<name %r>' % self.id

