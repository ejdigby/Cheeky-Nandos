from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", name=name)

@app.route("/quiz", method="GET")
def quiz():
	return render_template("quiz.html", name=name)

@app.route("/quiz", method="POST")
def quiz():
	return ("hello world")

if __name__ == "__main__": 
   app.run(host='0.0.0.0', port=5000)


