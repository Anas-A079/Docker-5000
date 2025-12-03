<<<<<<< HEAD
from flask import Flask
import redis
import os
import random
from datetime import datetime

app = Flask(__name__)

# Read Redis settings from environment
redis_host = os.environ.get("REDIS_HOST", "redis")
redis_port = int(os.environ.get("REDIS_PORT", 6379))

# Connect to Redis
r = redis.Redis(host=redis_host, port=redis_port, db=0)

@app.route("/")
def home():
    # Get visit count
    count = r.get("visits")
    if count is None:
        count = 1
    else:
        count = int(count.decode()) + 1
    r.set("visits", count)

    # Get last visit timestamp
    last_visit = r.get("last_visit")
    if last_visit:
        last_visit = last_visit.decode()
    else:
        last_visit = "No previous visits recorded."

    # Set new last visit timestamp
    r.set("last_visit", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # Random motivational quote
    quotes = [
        "Keep pushing forward! 🚀",
        "You’re doing great! 🌟",
        "Every refresh is a new opportunity.",
        "Made with ❤️ using Flask + Redis.",
        "Hello from your containerized app! 🐳",
        "Success is built one refresh at a time.",
        "Docker + Flask = Power combo!",
    ]
    quote = random.choice(quotes)

    # HTML output
    html = f"""
    <html>
      <body style="font-family: Arial, sans-serif; display: flex; flex-direction: column; align-items: center; margin-top: 50px;">
        <h1>Welcome to my Flask app!</h1>

        <div style="border: 2px solid black; padding: 20px; width: 350px; text-align: center; font-size: 20px; margin-top: 20px;">
          This page has been visited <b>{count}</b> times.
        </div>

        <p style="margin-top: 20px;">
          Last visit: <b>{last_visit}</b>
        </p>

        <p style="margin-top: 10px; font-style: italic; color: #555;">
          {quote}
        </p>
      </body>
    </html>
    """
    return html

@app.route("/count")
def count_page():
    return home()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
=======
# app.py

from flask import Flask
import MySQLdb

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="mydb",    # Hostname of the MySQL container
        user="root",    # Username to connect to MySQL
        passwd="my-secret-pw",  # Password for the MySQL user
        db="mysql"      # Name of the database to connect to
    )
    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()
    return f'Hello, World! MySQL version: {version[0]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> c1c685270a14c86ac9451a75d79194140ef219e1
