
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("registration.html")

@app.route('/register', methods=['POST'])
def registration():
    student_name = request.form['student_name']
    roll_number = request.form['roll_number']

    return render_template(
        "registrationsuccess.html",
        student_name=student_name,
        roll_number=roll_number
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
