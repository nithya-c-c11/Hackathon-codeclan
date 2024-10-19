from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    type = db.Column(db.String(10))  # 'theory' or 'lab'

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))

@app.route('/api/enroll/', methods=['POST'])
def enroll():
    data = request.json
    for selection in data['course_selections']:
        enrollment = Enrollment(
            student_id=data['student_id'],
            course_id=selection['course_id'],
            teacher_id=selection['teacher_id']
        )
        db.session.add(enrollment)
    db.session.commit()
    return jsonify({"message": "Enrollment successful"}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
