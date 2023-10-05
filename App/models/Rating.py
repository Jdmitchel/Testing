from App.database import db


class Rating(db.Model):
    ratingId = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.Integer, db.ForeignKey('student.studentId'), nullable=False)
    teacherId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    titleText = db.Column(db.String, nullable=False)

    def __init__(self, ratingId, titleText):
        self.ratingId = ratingId
        self.titleText = titleText

    def get_json(self):
        return {
            'ratingId': self.ratingId,
            'studentId': self.studentId,
            'teacherId': self.teacherId,
            'titleText': self.titleText
        }
        