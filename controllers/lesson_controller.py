from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.lesson import Lesson
import repositories.lesson_repository as lesson_repository

lessons_blueprint = Blueprint("lessons", __name__)

@lessons_blueprint.route("/lessons")
def lessons():


@lessons_blueprint.route("/lessons/<id>")
def show_lesson(id):


@lessons_blueprint.route("/lessons/new")
def new_lesson(id):


@lessons_blueprint.route("/lessons/<id>/delete")
def delete_lesson(id):