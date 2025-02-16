# pip install flask flask-cors firebase-admin

from flask import Flask
from flask import Flask, request, jsonify
from flask import Flask, request, render_template
from flask_cors import CORS
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__, template_folder="templates")
CORS(app)

cred = credentials.Certificate("key.json")
initialize_app(cred)
db = firestore.client()

@app.route("/", methods = ["GET","POST"])
def hello_world():
    return render_template("front.html")
    #return jsonify({"Hello": "name"})


# http://localhost:5000/add-numbers?num1=10&num2=20
@app.route("/add-numbers")
def add_numbers():
    num1 = int(request.args.get("num1"))
    num2 = int(request.args.get("num2"))
    return {"result": num1 + num2}


# http://localhost:5000/add?name=Jake&email=blah%40example.com
@app.route("/add")
def add_document():
    name = request.args.get("name")
    email = request.args.get("email")
    data = {"name": name, "email": email}
    doc_ref = db.collection("COLLECTION").add(data)
    return jsonify({"id": doc_ref[1].id})


# http://localhost:5000/get-doc?id=abc123
@app.route("/get-doc")
def get_document():
    doc_id = request.args.get("id")
    doc_ref = db.collection("COLLECTION").document(doc_id)
    doc = doc_ref.get()
    if doc.exists:
        return jsonify(doc.to_dict())
    else:
        return jsonify({"error": "Document not found"})


if __name__ == "__main__":
    app.run(debug=True)
