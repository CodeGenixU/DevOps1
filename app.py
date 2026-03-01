from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DATABASE_URI = 'sqlite:///data.db'

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Student(db.Model):
    roll = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    father_name = db.Column(db.String(80), nullable=False)
    mother_name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(10), nullable=False)

@app.route('/', methods = ['GET'])
def index():
    return jsonify({"status": "success"}), 200

@app.route("/add", methods=["POST"])
def add_student():
    data = request.get_json()
    roll = data["roll"]
    name = data["name"]
    father_name = data["father_name"]
    mother_name = data["mother_name"]
    gender = data["gender"]
    email = data["email"]
    phone = data["phone"]
    student = Student(roll=roll, name=name, father_name=father_name, mother_name=mother_name, gender=gender, email=email, phone=phone)
    db.session.add(student)
    db.session.commit()
    return jsonify({"status": "success"}), 200

@app.route("/student/<roll>", methods=["GET"])
def student(roll):
    student = Student.query.filter_by(roll=roll).first()
    if student is None:
        return jsonify({"status": "error", "message": "Student not found"}), 404
    return jsonify({
        "status": "success",
        "data": {
            "roll": student.roll,
            "name": student.name,
            "father_name": student.father_name,
            "mother_name": student.mother_name,
            "gender": student.gender,
            "email": student.email,
            "phone": student.phone
        }
    }), 200
@app.route("/student/<roll>", methods=["DELETE"])
def delete_student(roll):
    student = Student.query.filter_by(roll=roll).first()
    if student is None:
        return jsonify({"status": "error", "message": "Student not found"}), 404
    db.session.delete(student)
    db.session.commit()
    return jsonify({"status": "success"}), 200

@app.route("/student/<roll>", methods=["PUT"])
def update_student(roll):
    data = request.get_json()
    student = Student.query.filter_by(roll=roll).first()
    if student is None:
        return jsonify({"status": "error", "message": "Student not found"}), 404
    student.name = data["name"]
    student.father_name = data["father_name"]
    student.mother_name = data["mother_name"]
    student.gender = data["gender"]
    student.email = data["email"]
    student.phone = data["phone"]
    db.session.commit()
    return jsonify({"status": "success"}), 200

@app.route("/student/<roll>", methods=["PATCH"])
def partial_update_student(roll):
    data = request.get_json()
    student = Student.query.filter_by(roll=roll).first()
    if student is None:
        return jsonify({"status": "error", "message": "Student not found"}), 404
    if "name" in data:
        student.name = data["name"]
    if "father_name" in data:
        student.father_name = data["father_name"]
    if "mother_name" in data:
        student.mother_name = data["mother_name"]
    if "gender" in data:
        student.gender = data["gender"]
    if "email" in data:
        student.email = data["email"]
    if "phone" in data:
        student.phone = data["phone"]
    db.session.commit()
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port = 24655, debug=True)