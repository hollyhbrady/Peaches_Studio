from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

@members_blueprint.route("/members/add", methods=['GET'])
def members_form():
    return render_template('members/new.html', title='Add Member', result='result')

@members_blueprint.route('/members/add', methods=["POST"])
def members_add():
    name = request.form["name"]
    membership = request.form["membership"]
    new_member = Member(name, membership)
    # member_repository.save(new_member)
    return render_template('/members/new.html', title='Member Added', result=member_repository.save(new_member))
    


# @members_blueprint.route("/members/<id>")
# def show_member(id):
