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
    member = request.form["member"]
    lesson = request.form["lesson"]
    new_booking = Booking(member, lesson)
    return render_template('/bookings/new.html', title='Booking Added', result=booking_repository.save(new_booking))


# @bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
# def delete_booking(id):