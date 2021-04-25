from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

# @members_blueprint.route("/members")
# def members():


# @members_blueprint.route("/members/<id>")
# def show_member(id):
