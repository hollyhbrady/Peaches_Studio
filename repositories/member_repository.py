from db.run_sql import run_sql

from models.booking import Booking
from models.lesson import Lesson
from models.member import Member

import repositories.lesson_repository as lesson_repository
import repositories.booking_repository as booking_repository

def save(member):
    sql = "INSERT INTO members (name, membership) VALUES (%s, %s) RETURNING id"
    values = [member.name, member.membership]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return f"New member {member.name} has been saved!"


def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['name'], result['membership'], result['id'])
    return member


def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['name'], row['membership'], row['id'])
        members.append(member)
    return members


def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def update(member):
    sql = "UPDATE members SET (name, membership) = (%s, %s) WHERE id = %s"
    values = [member.name, member.membership, member.id]
    run_sql(sql, values)


# SELECT FROM LESSONS WHERE A MEMBER IS...
def lessons(member):
    lessons = []
    sql = "SELECT lessons.* FROM lessons INNER JOIN bookings ON bookings.lesson_id = lessons.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        lesson = Lesson(row['name'], row['capacity'], row['category'], row['day'], row['time'], row['duration'], row['id'])
        lessons.append(lesson)
    return lessons
    # f"{lesson.name} on {lessons.day} at {lessons.time}"