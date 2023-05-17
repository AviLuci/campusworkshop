"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7nj5269vf5qb9jn50-a.oregon-postgres.render.com",
        database="todo_znrd",
        user="todo_znrd_user",
        password="zLDqKmJ6eqpKNzfbucLy3SDzA4lXP0p0")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes