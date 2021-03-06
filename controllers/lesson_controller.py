from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.lesson import Lesson
import repositories.lesson_repository as lesson_repository
import repositories.booking_repository as booking_repository

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

@lessons_blueprint.route("/lessons/<id>", methods=['GET'])
def show_lesson(id):
    lesson = lesson_repository.select(id)
    members = lesson_repository.members_in(lesson)
    vacancy = booking_repository.show_capacity(id)
    return render_template('lessons/show.html', lesson = lesson, members = members, vacancy = vacancy)

@lessons_blueprint.route("/lessons/<id>/edit", methods=['GET'])
def lessons_edit(id):
    lesson = lesson_repository.select(id)
    return render_template('/lessons/edit.html', lesson = lesson)

@lessons_blueprint.route("/lessons/<id>", methods=['POST'])
def lessons_update(id):
    name = request.form['name']
    capacity = request.form['capacity']
    category = request.form['category']
    day = request.form['day']
    time = request.form['time']
    duration = request.form['duration']
    lesson = Lesson(name, capacity, category, day, time, duration, id)
    lesson_repository.update(lesson)
    return redirect('/lessons')

@lessons_blueprint.route("/lessons/<id>/delete", methods=['POST'])
def lessons_delete(id):
    lesson_repository.delete(id)
    return redirect('/lessons')



# @lessons_blueprint.route("/lessons/<id>/delete")
# def delete_lesson(id):