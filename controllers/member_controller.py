from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
from models.session import Session
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repository.select(id)
    sessions = member_repository.sessions(member)
    return render_template("members/show.html", member=member, sessions=sessions)

@members_blueprint.route("/members/new", methods=['GET'])
def new_member():
    members = member_repository.select_all()
    return render_template("members/new.html", all_members=members)

@members_blueprint.route("/members", methods=['POST'])
def create_session():
    name = request.form['name']
    age = request.form['age']
    member = Member(name, age)
    member_repository.save(member)
    return redirect("/members")