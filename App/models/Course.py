from App.database import db


class Course(db.Model):
    courseId = db.Column(db.Integer, primary_key=True)
    staffId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    facultyId = db.Column(db.Integer, db.ForeignKey('faculty.facultyId'), nullable=False)
    studentName = db.Column(db.String, nullable=False, unique=True)
    degree = db.Column(db.String, nullable=False, unique=True)
    karma = db.Column(db.Integer, nullable=False, unique=True)

    def __init__(self, studentNme, degree, karma):
        self.studentName = studentNme
        self.degree = degree
        self.karma = karma

    def get_json(self):
        return {
            'courseId': self.courseId,
            'staffId': self.staffId,
            'facultyId': self.facultyId,
            'studentName': self.studentName,
            'degree': self.degree,
            'karma': self.karma
        }

