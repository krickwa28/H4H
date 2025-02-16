# pip install flask flask-cors firebase-admin render_template

from flask import Flask
from flask import Flask, request, jsonify
from flask import Flask, request, render_template
from flask_cors import CORS
from firebase_admin import credentials, firestore, initialize_app
from PIL import Image

app = Flask(__name__, template_folder="templates", static_folder="staticFiles")
CORS(app)

id = 0
pics = 15

app.secret_key = '[secretkey]'

cred = credentials.Certificate("key.json")
initialize_app(cred)
db = firestore.client()

@app.route("/")
def loginPage():
    return render_template("front.html") 

@app.route("/logout")
def logout():
    return render_template('front.html')

@app.route("/homePage")
def homePage():
    return render_template("home.html")

@app.route("/attempt.py")
def homeScreen():
    global id
    name=request.args.get("username")
    if name == "":
        return render_template("front.html")
    try:
        search_name=request.args.get("username")
        docs = db.collection("names").where("name","==",search_name).get()
        results = [doc for doc in docs]
        if results:
            id = results[0].id
        else:
            data = {"name": name, "weight": 0,}
            doc_ref = db.collection("names").add(data)
            id = doc_ref[1].id
        print (id)
    except Exception as e:
        return jsonify({"success1": False, "error": str(e)}),500
    return render_template("home.html")

@app.route("/addPlastic")
def addPlasticScreen():
    return render_template("buttons.html")

@app.route("/recyclingInfo")
def recyclingInfo():
    return render_template("recyclinginfo.html")

@app.route("/whatCounts")
def whatCounts():
    return render_template("what.html")

@app.route("/Bottles")
def bottlesButton():
    global id
    print (id)
    try:
        doc_ref = db.collection("names").document(id)
        doc_snapshot = doc_ref.get()
        doc_ref.update({"weight": firestore.Increment(2)})
        weight = doc_ref.get().to_dict()["weight"]
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}),500
    if weight <= 5:
        plastic = "light"
    elif weight <= 10:
        plastic = "medium"
    else:
        plastic = "heavy"
    return render_template("home.html", plastic=plastic)

@app.route("/Utensils")
def utensilsButton():
    global id
    print (id)
    try:
        doc_ref = db.collection("names").document(id)
        doc_snapshot = doc_ref.get()
        doc_ref.update({"weight": firestore.Increment(1)})
        weight = doc_ref.get().to_dict()["weight"]
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}),500
    if weight <= 5:
        plastic = "light"
    elif weight <= 10:
        plastic = "medium"
    else:
        plastic = "heavy"
    return render_template("home.html", plastic=plastic)

@app.route("/Bags")
def bagsButton():
    global id
    print (id)
    try:
        doc_ref = db.collection("names").document(id)
        doc_snapshot = doc_ref.get()
        doc_ref.update({"weight": firestore.Increment(3)})
        weight = doc_ref.get().to_dict()["weight"]
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}),500
    if weight <= 5:
        plastic = "light"
    elif weight <= 10:
        plastic = "medium"
    else:
        plastic = "heavy"
    return render_template("home.html", plastic=plastic)

@app.route("/Containers")
def containersButton():
    global id
    print (id)
    try:
        doc_ref = db.collection("names").document(id)
        doc_snapshot = doc_ref.get()
        doc_ref.update({"weight": firestore.Increment(3)})
        weight = doc_ref.get().to_dict()["weight"]
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}),500
    if weight <= 5:
        plastic = "light"
    elif weight <= 10:
        plastic = "medium"
    else:
        plastic = "heavy"
    return render_template("home.html", plastic=plastic)

@app.route("/Other")
def otherButton():
    global id
    global pics
    print (id)
    try:
        doc_ref = db.collection("names").document(id)
        doc_snapshot = doc_ref.get()
        doc_ref.update({"weight": firestore.Increment(2)})
        weight = doc_ref.get().to_dict()["weight"]
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}),500
    if weight <= 5:
        plastic = "light"
    elif weight <= 10:
        plastic = "medium"
    else:
        plastic = "heavy"
    return render_template("home.html", plastic=plastic)

@app.route("/None")
def noPlastic():
    return render_template("animal.html")

if __name__ == "__main__":
    app.run(debug=True)
