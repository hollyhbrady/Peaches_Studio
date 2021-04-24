from db.run_sql import run_sql

from models.booking import Booking
from models.lesson import Lesson
from models.member import Member

import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

def save(lesson):
    sql = "INSERT INTO lessons (name, capacity, category, day, time, duration) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [lesson.name, lesson.capacity, lesson.category, lesson.day, lesson.time, lesson.duration]
    results = run_sql(sql, values)
    lesson.id = results[0]['id']
    return lesson


def select(id):
    pass


def select_all():
    pass


def delete(id):
    pass


def delete_all():
    pass


def members(lesson):
    pass #FIND ALL MEMBERS BOOKED FOR A LESSON
