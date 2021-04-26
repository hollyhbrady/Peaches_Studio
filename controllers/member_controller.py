from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository

import pdb

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

@members_blueprint.route("/members/new", methods=['GET'])
def members_form():
    return render_template('members/new.html', title='Add Member')

@members_blueprint.route("/members/new", methods=['POST'])
def members_add():
    name = request.form["name"]
    membership = request.form["membership"]
    new_member = Member(name, membership)
    return render_template('/members/new.html', title='Member Added', result=member_repository.save(new_member))
    
@members_blueprint.route("/members/<id>", methods=['GET'])
def members_show(id):
    member = member_repository.select(id)
    lessons = member_repository.lessons(member)
    return render_template('/members/show.html', member = member, lessons=lessons)

@members_blueprint.route("/members/<id>/edit", methods=['GET'])
def members_edit(id):
    member = member_repository.select(id)
    return render_template('/members/edit.html', member = member)

@members_blueprint.route("/members/<id>", methods=['POST'])
def members_update(id):
    name = request.form["name"]
    membership = request.form["membership"]
    member = Member(name, membership, id)
    member_repository.update(member)
    return redirect('/members')

@members_blueprint.route("/members/<id>/delete", methods=['POST'])
def members_delete(id):
    member_repository.delete(id)
    return redirect('/members')

