from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "Believe in yourself!",
    "Stay positive and happy.",
    "Work hard and don’t give up hope.",
    "Be open to criticism and keep learning.",
    "Stay focused and never give up."
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quote')
def get_quote():
    return random.choice(quotes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
