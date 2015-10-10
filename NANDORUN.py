from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/quiz", methods=['GET', 'POST'])
def quiz():
	if request.method == 'POST':

		answers = []
		totalscore = 0
		for i in range(1, 12):
			answers.append(request.form["q" + str(i)])


		for i in answers:
			if i == 0 or i == 4 or i == 5:
				totalscore += i * 20
			elif i == 1 or i == 2:
				totalscore += i * 10
			elif i == 3:
				totalscore += i * 25
			elif i == 6 or i==7 or i == 8 or i == 9 or i==10:
				 if answers[i] == "NO":
				 	totalscore -= 10
				 elif answers[i] == "YES":
				 	totalscore += 100
				 else:
				 	print "error"

		print totalscore
		return ("hello world")
	else:
		return render_template("quiz.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
