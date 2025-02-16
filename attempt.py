# pip install flask flask-cors firebase-admin render_template

from flask import Flask
from flask import Flask, request, jsonify
from flask import Flask, request, render_template
from flask_cors import CORS
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__, template_folder="templates")
CORS(app)

app.secret_key = '[secretkey]'

cred = credentials.Certificate("key.json")
initialize_app(cred)
db = firestore.client()

@app.route("/")
def loginPage():
    return render_template("front.html") 

@app.route("/attempt.py")
def homeScreen():
    name = request.args.get("username")
    data = {"name": name}
    doc_ref = db.collection("names").add(data)
    return "Hello, {}!" .format(name), 
#render_template("home.php")

if __name__ == "__main__":
    app.run(debug=True)

