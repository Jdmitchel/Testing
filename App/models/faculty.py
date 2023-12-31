from App.database import db


class Faculty(db.Model):
    facultyId = db.Column(db.Integer, primary_key=True)
    facultyName = db.Column(db.String, nullable=False, unique=True)

    students = db.relationship('Student', backref='faculty', lazy=True)
    courses = db.relationship('Course', backref='faculty', lazy=True)

    def __init__(self, facultyName):
        self.facultyName = facultyName

