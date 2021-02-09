import os
import sys
import psycopg2
import traceback
from psycopg2 import Error


DATABASE_URL = os.getenv('DATABASE_URL')


def post_sql_query(sql_query):
    connection = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = connection.cursor()
    data = []
    try:
        cursor.execute(sql_query)
        data = cursor.fetchall()
    except psycopg2.ProgrammingError:
        pass
    finally:
        cursor.close()
        # commit the changes
        connection.commit()
        return data


def input_new_user(user_id: str, phone: str):
    sql_selection = f"SELECT * FROM users WHERE "\
                    f"user_id = '{user_id}';"
    rows = post_sql_query(sql_selection)
    if not rows:
        query = f"INSERT INTO users (user_id, phone) VALUES ('{user_id}', "\
                f"'{phone}';"
        post_sql_query(query)


def create_table():
    query = '''CREATE TABLE IF NOT EXISTS users
                        (user_id PRIMARY KEY,
                        phone VARCHAR(255));'''
    connection = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = connection.cursor()
    cursor.execute(query)
    # close communication with the PostgreSQL database server
    cursor.close()
    # commit the changes
    connection.commit()
