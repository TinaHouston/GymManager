from db.run_sql import run_sql

from models.session import Session
from models.member import Member

def save(session):
    sql = "INSERT INTO sessions(name, capacity, time, date) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [session.name, session.capacity, session.time, session.date]
    results = run_sql(sql, values)
    session.id = results[0]['id']
    return session

def select_all():
    sessions = []

    sql = "SELECT * FROM sessions"
    results = run_sql(sql)

    for row in results:
        session = Session(row['name'], row['capacity'], row['time'], row['date'], row['id'])
        sessions.append(session)
    return sessions

def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)