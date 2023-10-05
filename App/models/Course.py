from App.database import db


class Course(db.Model):
    courseId = db.Column(db.Integer, primary_key=True)
    staffId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    facultyId = db.Column(db.Integer, db.ForeignKey('faculty.facultyId'), nullable=False)
    courseName = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, courseName, courseId):
        self.courseId = courseId
        self.courseName = courseName

    def get_json(self):
        return {
            'courseId': self.courseId,
            'staffId': self.staffId,
            'facultyId': self.facultyId,
            'courseName': self.courseName
            
        }

