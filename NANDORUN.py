from flask import Flask
app = Flask(__Nando's-Cheekiness-Calculator__)

@app.route("/")
def hello():
    return "Hello World!"