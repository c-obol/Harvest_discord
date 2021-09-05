from flask import Flask
from flask.templating import render_template
import bot

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    bot.run()
    app.run(host = '127.0.0.1', port = '5000')