from models import db, TeacherRating
from sqlalchemy import func

def get_teacher_average_rating(teacher_id):
    avg_rating = db.session.query(func.avg(TeacherRating.rating)).filter(TeacherRating.teacher_id == teacher_id).scalar()
    return round(avg_rating, 2) if avg_rating else None