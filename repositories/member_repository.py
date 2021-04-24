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
    pass


def select_all():
    pass


def delete(id):
    pass


def delete_all():
    pass


def lessons(member):
    pass #find all lessons a member is booked on