from App.database import db
from flask_security import UserMixin, RoleMixin


class Student(db.Model, UserMixin):
    studentId = db.Column(db.Integer, primary_key=True)
    facultyId = db.Column(db.Integer, db.ForeignKey('faculty.facultyId'), nullable=False)
    studentName = db.Column(db.String, nullable=False, unique=True)
    degree = db.Column(db.String, nullable=False, unique=True)
    karma = db.Column(db.Integer, nullable=False, unique=True)

    studentRatings = db.relationship('Rating', backref='student', lazy=True)

    def __init__(self, studentNme, degree, karma):
        self.studentName = studentNme
        self.degree = degree
        self.karma = karma
    
    def get_json(self):
        return {
            'studentId': self.studentId,
            'facultyId': self.facultyId,
            'studentName': self.studentName,
            'degree': self.degree,
            'karma': self.karma
        }


@app.before_first_request
def create_tables():
    db.create_all()