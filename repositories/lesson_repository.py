from db.run_sql import run_sql

from models.booking import Booking
from models.lesson import Lesson
from models.member import Member

import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

import pdb

def save(lesson):
    sql = "INSERT INTO lessons (name, capacity, category, day, time, duration) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [lesson.name, lesson.capacity, lesson.category, lesson.day, lesson.time, lesson.duration]
    results = run_sql(sql, values)
    id = results[0]['id']
    lesson.id = id
    return f"New lesson {lesson.name} on {lesson.day} at {lesson.time} has been saved!"


def select(id):
    lesson = None
    sql = "SELECT * FROM lessons WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]

    if results is not None:
        lesson = Lesson(results['name'], results['capacity'], results['category'], results['day'], results['time'], results['duration'], results['id'])
    return lesson

def select_all():
    lessons = []
    sql = "SELECT * FROM lessons"
    results = run_sql(sql)

    for row in results:
        lesson = Lesson(row['name'], row['capacity'], row['category'], row['day'], row['time'], row['duration'], row['id'])
        lessons.append(lesson)
    return lessons


def delete(id):
    sql = "DELETE FROM lessons WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM lessons"
    run_sql(sql)

def update(lesson):
    sql = "UPDATE lessons SET (name, capacity, category, day, time, duration) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [lesson.name, lesson.capacity, lesson.category, lesson.day, lesson.time, lesson.duration, lesson.id]
    run_sql(sql, values)


# SELECT FROM MEMBERS WHERE LESSON IS...
def members_in(lesson):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings on bookings.member_id = members.id WHERE lesson_id = %s"
    values = [lesson.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['name'], row['membership'], row['id'])
        members.append(member)
    return members

