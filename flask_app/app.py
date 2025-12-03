from flask import Flask
import redis
import os
import random
from datetime import datetime

app = Flask(__name__)

# Redis config
redis_host = os.environ.get("REDIS_HOST", "redis")
redis_port = int(os.environ.get("REDIS_PORT", 6379))
r = redis.Redis(host=redis_host, port=redis_port, db=0)

@app.route("/")
def home():
    count = r.get("visits")
    count = 1 if count is None else int(count.decode()) + 1
    r.set("visits", count)

    last_visit = r.get("last_visit")
    last_visit = last_visit.decode() if last_visit else "No previous visits."
    r.set("last_visit", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

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

    return f"""
    <html>
      <body style="font-family: Arial; text-align:center; margin-top:50px;">
        <h1>Welcome to my Flask app!</h1>
        <div style="border:2px solid black; padding:20px; width:350px; margin:auto;">
          This page has been visited <b>{count}</b> times.
        </div>
        <p>Last visit: <b>{last_visit}</b></p>
        <p style="font-style:italic; color:#555;">{quote}</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
