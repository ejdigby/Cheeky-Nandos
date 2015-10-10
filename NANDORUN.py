from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz", methods="GET")
def quiz():
	return render_template("quiz.html")

@app.route("/quiz", methods="POST")
def quizanswers():
	return ("hello world")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
