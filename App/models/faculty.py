from App.database import db
from flask_security import UserMixin, RoleMixin


class Faculty(db.Model, UserMixin):
    facultyId = db.Column(db.Integer, primary_key=True)
    facultyName = db.Column(db.String, nullable=False, unique=True)

    students = db.relationship('Student', backref='faculty', lazy=True)
    courses = db.relationship('Courses', backref='faculty', lazy=True)

    def __init__(self, facultyName):
        self.facultyName = facultyName

    


@app.before_first_request
def create_tables():
    db.create_all()