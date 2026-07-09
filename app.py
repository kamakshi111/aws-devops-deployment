from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [
    {
        "id": 1,
        "name": "Kamakshi",
        "role": "DevOps Engineer"
    },
    {
        "id": 2,
        "name": "Rahul",
        "role": "Python Developer"
    }
]


@app.route("/")
def home():
    return jsonify({
        "message": "AWS DevOps Assignment",
        "status": "Running Successfully"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "Healthy"
    })


@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)


@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.get_json()

    employee = {
        "id": len(employees) + 1,
        "name": data["name"],
        "role": data["role"]
    }

    employees.append(employee)

    return jsonify(employee), 201


@app.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):
    data = request.get_json()

    for employee in employees:
        if employee["id"] == id:
            employee["name"] = data["name"]
            employee["role"] = data["role"]
            return jsonify(employee)

    return jsonify({"message": "Employee not found"}), 404


@app.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):
    for employee in employees:
        if employee["id"] == id:
            employees.remove(employee)
            return jsonify({"message": "Employee deleted"})

    return jsonify({"message": "Employee not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)