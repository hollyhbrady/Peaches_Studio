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
    return member

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
    pass


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)


def lessons(member):
    pass #find all lessons a member is booked on