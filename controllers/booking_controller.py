from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository


bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings = bookings)

@bookings_blueprint.route("/bookings/new", methods=['GET'])
def booking_form():
    members = member_repository.select_all()
    lessons = lesson_repository.select_all()
    return render_template("/bookings/new.html", title="Add Booking", members = members, lessons = lessons)

@bookings_blueprint.route("/bookings/new", methods=['POST'])
def booking_add():
    member_id = request.form['member_id']
    lesson_id = request.form['lesson_id']
    member = member_repository.select(member_id)
    lesson = lesson_repository.select(lesson_id)
    new_booking = Booking(member, lesson)
    result = booking_repository.save(new_booking)
    return render_template('/bookings/new.html', title='Booking Added')

# @bookings_blueprint.route("/bookings/<id>", methods=['GET'])
# def bookings_show(id):

# @bookings_blueprint.route("/bookings/<id>/edit", methods=['GET'])
# def bookings_edit(id):

#     @bookings_blueprint.route("/bookings/<id>", methods=['POST'])
# def bookings_update(id):


# @bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
# def delete_booking(id):