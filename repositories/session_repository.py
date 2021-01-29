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

def select(id):
    session = None
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        session = Session(result['name'], result['capacity'], result['time'], result['date'], result['id'])
    return session

def members(session):
    members = []

    sql = "SELECT members.* from members INNER JOIN bookings ON bookings.member_id = members.id WHERE session_id = %s"
    values = [session.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['name'], row['age'], row['id'])
        members.append(member)
    return members

def delete(id):
    sql = "DELETE FROM sessions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(session):
    sql = "UPDATE sessions SET (name, capacity, time, date) = (%s, %s, %s, %s) WHERE id = %s"
    values = [session.name, session.capacity, session.time, session.date, session.id]
    print(values)
    run_sql(sql, values)