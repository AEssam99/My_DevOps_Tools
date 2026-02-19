from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('POSTGRES_HOST'),
        database=os.environ.get('POSTGRES_DB'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD')
    )
    return conn

@app.route('/')
def home():
    return jsonify({"message": "Flask + PostgreSQL setup works!"})

@app.route('/users')
def users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT);')
    cur.execute('INSERT INTO users (name) VALUES (%s) RETURNING id;', ('Ahmed',))
    conn.commit()
    cur.execute('SELECT * FROM users;')
    result = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)