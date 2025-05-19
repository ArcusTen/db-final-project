from flask import Flask, jsonify, request, render_template, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = 'mypass'       # change it later !!

DATABASE = os.path.join(os.path.dirname(__file__), 'db', 'alumni_dms.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/alumni', methods=['GET'])
def get_alumni():
    conn = get_db_connection()
    alumni = conn.execute('SELECT * FROM alumni').fetchall()
    conn.close()
    return jsonify([dict(row) for row in alumni])

@app.route('/api/events', methods=['GET'])
def get_events():
    conn = get_db_connection()
    events = conn.execute('SELECT * FROM events').fetchall()
    conn.close()
    return jsonify([dict(row) for row in events])

@app.route('/api/registrations', methods=['POST'])
def register_event():
    new_registration = request.get_json()
    conn = get_db_connection()
    conn.execute('INSERT INTO event_registrations (alumni_id, event_id) VALUES (?, ?)',
                 (new_registration['alumni_id'], new_registration['event_id']))
    conn.commit()
    conn.close()
    return jsonify(new_registration), 201

@app.route('/api/donations', methods=['POST'])
def make_donation():
    new_donation = request.get_json()
    conn = get_db_connection()
    conn.execute('INSERT INTO donations (alumni_id, amount) VALUES (?, ?)',
                 (new_donation['alumni_id'], new_donation['amount']))
    conn.commit()
    conn.close()
    return jsonify(new_donation), 201

@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    feedback = request.get_json()
    conn = get_db_connection()
    conn.execute('INSERT INTO feedback (alumni_id, message) VALUES (?, ?)',
                 (feedback['alumni_id'], feedback['message']))
    conn.commit()
    conn.close()
    return jsonify(feedback), 201

@app.route('/api/job_postings', methods=['GET'])
def get_job_postings():
    conn = get_db_connection()
    job_postings = conn.execute('SELECT * FROM job_postings').fetchall()
    conn.close()
    return jsonify([dict(row) for row in job_postings])

@app.route('/api/signup', methods=['POST'])
def signup():
    # Use form data instead of JSON
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400

    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
    if user:
        conn.close()
        return jsonify({'error': 'User already exists'}), 409

    hashed_password = generate_password_hash(password)
    conn.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, hashed_password))
    conn.commit()
    conn.close()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/api/signin', methods=['POST'])
def signin():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400

    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
    conn.close()
    if user and check_password_hash(user['password'], password):
        session['user_id'] = user['id']
        return jsonify({'message': 'Sign in successful'}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Create users table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    # Add other tables here as needed
    conn.commit()
    conn.close()

# Initialize DB on app startup
init_db()

if __name__ == '__main__':
    app.run(debug=True)