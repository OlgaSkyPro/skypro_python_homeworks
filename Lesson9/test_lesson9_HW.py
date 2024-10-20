import pytest
import requests

from sqlalchemy import create_engine
from sqlalchemy import text

db_connection_string = 'postgresql://postgre:NoveNove_93@localhost:5432/postgres'

def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from subject").fetchall()
    row1 = rows[0]

    assert row1["subject_title"] == "Mathematics"


def test_insert():
    db = create_engine(db_connection_string)
    db.execute('''INSERT into subject (subject_id, subject_title) VALUES(17, 'Algebra');''')
    rows = db.execute("select * from subject").fetchall()
    row1=rows[-1]
    sql = text("DELETE FROM subject WHERE subject_id = :id")
    db.execute(sql, id=17)
    assert row1["subject_title"] == 'Algebra'

def test_update():
     db = create_engine(db_connection_string)
     db.execute('''INSERT into subject (subject_id, subject_title) VALUES(17, 'Algebra');''')
     rows = db.execute("select * from subject").fetchall()
     row1=rows[-1]
     sql = text("update subject set subject_title = :new_title where subject_id=:id")
     db.execute(sql, new_title = 'Matan', id = row1["subject_id"])
     rows = db.execute("select * from subject").fetchall()
     row2=rows[-1]
     sql = text("DELETE FROM subject WHERE subject_id = :id")
     id_update = row2["subject_id"]
     db.execute(sql, id=id_update)
     assert row2["subject_title"] == "Matan"


def test_delete():
    db = create_engine(db_connection_string)
    db.execute('''INSERT into subject (subject_id, subject_title) VALUES(17, 'Algebra');''')
    rows = db.execute("select * from subject").fetchall()
    row1=rows[-1]

    sql = text("DELETE FROM subject WHERE subject_id = :id")
    db.execute(sql, id=17)
    

