from db.run_sql import run_sql

from models.booking import Booking
from models.lesson import Lesson
from models.member import Member

import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository

def save(booking):
    lesson = lesson_repository.select(booking.lesson.id)
    # find capacity of this lesson
    capacity = booking.lesson.capacity
    # find how many people are booked on this lesson
    booked = lesson_repository.members_in(booking.lesson)
    schedule = member_repository.lessons(booking.member)
    # if statement: 
    # if booked < capacity:
    #   if people booked is less than capacity
    #   add to lesson
    #   else
    #   return string
    # if statement: 
    # if people booked is more than or equal to capacity

    if len(booked) >= capacity:
    #   return fail string
        return f"This lesson is already full, capacity of {booking.lesson.capacity} has been reached."
    for booked_member in booked:
        if booked_member.id == booking.member.id:
    # if booking.member.name in booked:
            return f"{booking.member.name} is already booked for this class."
    for schedule_member in schedule:
        if booking.member.membership == "Standard":
            if len(schedule) >= 3:
                return "Standard members can attend a maximum of 3 classes a week. Offer upgrade to Deluxe for unlimited classes."
    sql = "INSERT INTO bookings (member_id, lesson_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.lesson.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return f"New booking for {booking.member.name} has been made for {booking.lesson.name} on {booking.lesson.day}."


def select(id):
    booking = None
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        booking = Member(result['member'], result['lesson'], result['id'])
    return booking


def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        lesson = lesson_repository.select(row['lesson_id'])
        booking = Booking(member, lesson, row['id'])
        bookings.append(booking)
    return bookings


def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

# Not currently using
def update(booking):
    sql = "UPDATE bookings SET (member_id, lesson_id) = (%s, %s) WHERE id = %s"
    values = [booking.member.id, booking.lesson.id, lesson.id]
    run_sql(sql, values)

# def check_capacity(lesson_id):
#     # find lesson by id
#     lesson = lesson_repository.select(id)
#     # find capacity of this lesson
#     capacity = lesson.capacity
#     # find how many people are booked on this lesson
#     booked = lesson_repository.members_in(id)
#     # if statement: 
#     # if booked < capacity:
#     #   if people booked is less than capacity
#     #   add to lesson
#     #   else
#     #   return string
    
#     # if statement: 
#     # if people booked is more than or equal tocapacity
#         if len(booked) >= capacity:
#     #   return fail string
#             return "This lesson is already full"
#     #   else
#     #   continue? to save(booking)

    
def show_capacity(id):
    # find lesson by id
    lesson = lesson_repository.select(id)
    # find capacity of this lesson
    capacity = lesson.capacity
    # find how many people are booked on this lesson
    booked = lesson_repository.members_in(lesson)
    vacancy = capacity - len(booked)
    return vacancy
 

