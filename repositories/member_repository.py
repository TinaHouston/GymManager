from db.run_sql import run_sql

from models.session import Session
from models.member import Member

def save(member):
    sql = "INSERT INTO members(name, age) VALUES (%s, %s) RETURNING id"
    values = [member.name, member.age]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'], row['age'], row['id'])
        members.append(member)
    return members

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def select(id):
    user = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['name'], result['age'], result['id'])
    return member