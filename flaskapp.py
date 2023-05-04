from flask import Flask, jsonify, request

app =  Flask(__name__)

list = [
    {
        'id': 1,
        'Name': "Raju",
        "done": False,
        "Contact": "9987644456"
    },
    {

    'id': 2,
    'Name': "Rahul",
    "done": False
    'Contact': "8197696666"




    }
]

@app.route("/")
def halogen():
    return "hi"

@app.route("/", methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        },400)
    
    contact = {
        'id': tasks[-1]['id']+1,
        'Name': request.json['Name'],
        'Contact': request.json.get['Contact', ""],
        'done': False

    }

    list.append(contact)
    return jsonify({
        "status": "success",
        "message": "contact added successfully"
    
    })





