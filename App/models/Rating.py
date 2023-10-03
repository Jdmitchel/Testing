from App.database import db


class Rating(db.Model):
    ratingId = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.Integer, db.ForeignKey('student.studentId'), nullable=False)
    teacherId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    studentName = db.Column(db.String, nullable=False, unique=True)
    degree = db.Column(db.String, nullable=False, unique=True)
    karma = db.Column(db.Integer, nullable=False, unique=True)

    def __init__(self, studentName, degree, karma):
        self.studentName = studentName
        self.degree = degree
        self.karma = karma

    def get_json(self):
        return {
            'ratingId': self.ratingId,
            'studentId': self.studentId,
            'teacherId': self.teacherId,
            'studentName': self.studentName,
            'degree': self.degree,
            'karma': self.karma
        }
