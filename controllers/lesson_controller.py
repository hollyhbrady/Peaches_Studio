from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.lesson import Lesson
import repositories.lesson_repository as lesson_repository

lessons_blueprint = Blueprint("lessons", __name__)

@lessons_blueprint.route("/lessons")
def lessons():
    lessons = lesson_repository.select_all()
    return render_template("lessons/index.html", lessons = lessons)

@lessons_blueprint.route("/lessons/new", methods=['GET'])
def lesson_form():
    return render_template('lessons/new.html', title='Add Lesson')

@lessons_blueprint.route("/lessons/new", methods=['POST'])
def lessons_add():
    name = request.form['name']
    capacity = request.form['capacity']
    category = request.form['category']
    day = request.form['day']
    time = request.form['time']
    duration = request.form['duration']
    new_lesson = Lesson(name, capacity, category, day, time, duration)
    return render_template('lessons/new.html', title='Lesson Added', result=lesson_repository.save(new_lesson))

# @lessons_blueprint.route("/lessons/<id>")
# def show_lesson(id):



# @lessons_blueprint.route("/lessons/<id>/delete")
# def delete_lesson(id):