from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host='db', 
        database='mydb',
        user='user',
        password='password'
    )
    return conn

@app.route('/')
def hello():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT message FROM greetings LIMIT 1;')
    message = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(message=message[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
