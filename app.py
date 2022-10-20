from sqlite3 import connect
from flask import Flask
import psycopg2
import names

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to my App."

def getConnection():
    return psycopg2.connect(
        host="db",
        database="postgres",
        user="postgres",
        password="postgres"
    )

@app.route("/initialize")
def initialize():
    conn = getConnection()
    try:
        cur = conn.cursor()

        for _ in range(50):
            fname = names.get_first_name()
            lname = names.get_last_name()
            sql = f"""
                insert into public.profiles
                (last_name, first_name, email)
                VALUES
                ('{lname}', '{fname}', '{fname}.{lname}@gmail.com')
            """
            cur.execute(sql)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return "Failed to generate records"
    finally:
        if conn is not None:
            conn.close()
    return "Successfully generated names."

@app.route("/students")
def students():
    conn = getConnection()
    result = ""
    try:
        cur = conn.cursor()

        print("PostgreSQL database version:")
        cur.execute("SELECT * FROM public.profiles")

        recs=cur.fetchall()
        for rec in recs:
            result += rec[1] + " " + rec[2] + "<p>"
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        result = "Error"
    finally:
        if conn is not None:
            conn.close()
    return result

