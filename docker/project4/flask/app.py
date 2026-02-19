from flask import Flask, jsonify
import psycopg2
from config import Config

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=Config.POSTGRES_HOST,
        database=Config.POSTGRES_DB,
        user=Config.POSTGRES_USER,
        password=Config.POSTGRES_PASSWORD
    )
    return conn

@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask API!"})

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

@app.route('/testdb')
def test_db():
    try:
        conn = psycopg2.connect(
            host=Config.POSTGRES_HOST,
            database=Config.POSTGRES_DB,
            user=Config.POSTGRES_USER,
            password=Config.POSTGRES_PASSWORD
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({'status': 'connected', 'version': db_version})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)