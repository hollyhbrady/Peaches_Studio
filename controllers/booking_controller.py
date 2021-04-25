from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking

import repositories.booking_repository as booking_repository
import repositories.lesson_repository as lesson_repository
import repositories.member_repository as member_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("booking/index.html", bookings = bookings)


# @bookings_blueprint.route("/bookings/new", methods=['GET'])
# def new_booking():


# @bookings_blueprint.route("/bookings", methods=['POST'])
# def create_booking():


# @bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
# def delete_booking(id):