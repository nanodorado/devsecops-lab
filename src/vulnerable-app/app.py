from flask import Flask, request, session, redirect, url_for, render_template_string, make_response
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'thisisnotsecure'

DB = 'vulnapp.db'

def init_db():
    if not os.path.exists(DB):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
        c.execute('CREATE TABLE messages (id INTEGER PRIMARY KEY, user_id INTEGER, content TEXT)')
        c.execute('INSERT INTO users (username, password) VALUES ("admin", "admin123"), ("alice", "password"), ("bob", "123456")')
        c.execute('INSERT INTO messages (user_id, content) VALUES (1, "Top secret admin note."), (2, "Alice private message."), (3, "Bob personal memo.")')
        conn.commit()
        conn.close()

@app.after_request
def add_header(response):
    # Intentionally disclosing headers
    response.headers['X-Powered-By'] = 'Flask/2.1.0'
    return response

@app.route('/')
def index():
    username = session.get('username')
    return f'''
    <h1>Vulnerable App</h1>
    {"<p>Logged in as: " + username + "</p>" if username else ""}
    <ul>
        <li><a href="/login">Login</a></li>
        <li><a href="/search">Search</a></li>
        <li><a href="/admin">Admin Panel (IDOR)</a></li>
        <li><a href="/debug">Debug Info</a></li>
    </ul>
    '''

# Login page vulnerable to SQL Injection
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        # DELIBERATE SQLI
        query = f"SELECT username FROM users WHERE username='{user}' AND password='{pwd}'"
        c.execute(query)
        result = c.fetchone()
        if result:
            session['username'] = result[0]
            return redirect(url_for('index'))
        return "Login failed"
    return '''
    <form method="post">
        Username: <input name="username"><br>
        Password: <input name="password" type="password"><br>
        <input type="submit" value="Login">
    </form>
    '''

# Reflected XSS vulnerability
@app.route('/search')
def search():
    q = request.args.get('q', '')
    # NO escaping, vulnerable to XSS
    return render_template_string(f'<h3>Results for: {q}</h3>')

# IDOR - user can view arbitrary messages
@app.route('/admin')
def admin():
    if not session.get('username'):
        return redirect(url_for('login'))
    msg_id = request.args.get('msg', '1')
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    # DELIBERATE IDOR
    c.execute(f"SELECT content FROM messages WHERE id={msg_id}")
    row = c.fetchone()
    return f"<h4>Message: {row[0] if row else 'Not found'}</h4>"

# Debug info leak
@app.route('/debug')
def debug():
    return f"Debug Mode: True | Session: {dict(session)}"

# Log sensitive info (insecure)
@app.route('/log', methods=['POST'])
def log():
    data = request.form.get('log')
    with open("app.log", "a") as f:
        f.write(data + "\n")
    return "Logged."

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)