from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        'Contact': '9987644456',
        'Name': 'Raju',
        'done': False,
        'Id': 1
    },
    {
        'Contact': '9876543222',
        'Name': 'Rahul',
        'done': False,
        'Id': 2
    }
]


@app.route("/add-data", methods={"POST"})
def add_contact():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data!"
        }, 400)

    contact = {
        'Id': contacts[-1]['Id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status": "success",
        "message": "Task added succesfully!"
    })


@app.route("/get-data")
def get_contact():
    return jsonify({
        "data": contacts
    })


if (__name__ == "__main__"):
    app.run(debug=True)
