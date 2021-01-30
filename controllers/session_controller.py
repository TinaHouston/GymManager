from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.session import Session
import repositories.session_repository as session_repository

sessions_blueprint = Blueprint("sessions", __name__)

@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all()
    return render_template("sessions/index.html", sessions=sessions)

@sessions_blueprint.route("/sessions/<id>")
def show(id):
    session = session_repository.select(id)
    members = session_repository.members(session)
    return render_template("sessions/show.html", session=session, members=members)

@sessions_blueprint.route("/sessions/new", methods=['GET'])
def new_session():
    sessions = session_repository.select_all()
    return render_template("sessions/new.html", all_sessions=sessions)

@sessions_blueprint.route("/sessions", methods=['POST'])
def create_session():
    name = request.form['name']
    capacity = request.form['capacity']
    time = request.form['time']
    date = request.form['date']
    session = Session(name, capacity, time, date)
    session_repository.save(session)
    return redirect("/sessions")

@sessions_blueprint.route("/sessions/<id>/edit", methods = ['GET'])
def edit_session(id):
    session = session_repository.select(id)
    return render_template("sessions/edit.html", session = session)

@sessions_blueprint.route("/sessions/<id>", methods = ['POST'])
def update_class(id):
    name = request.form['name']
    capacity = request.form['capacity']
    time = request.form['time']
    date = request.form['date']
    session = Session(name, capacity, time, date, id)
    session_repository.update(session)
    return redirect("/sessions")

@sessions_blueprint.route("/sessions/filter")
def show_available_sessions():
    sessions = session_repository.select_all()
    return render_template("/sessions/filter.html", sessions=sessions)