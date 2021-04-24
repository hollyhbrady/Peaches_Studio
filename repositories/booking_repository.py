from db.run_sql import run_sql

from models.booking import Booking
from models.lesson import Lesson
from models.member import Member

import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository

def save(booking):
    sql = "INSERT INTO bookings (member_id, lesson_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.lesson.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking


def select(id):
    pass


def select_all():
    pass


def delete(id):
    pass


def delete_all():
    pass
