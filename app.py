from flask import Flask

app = Flask(__name__)


@app.route('/')
def Home():
    return {
        "message": "Home page",
        "success": True
    }


@app.route('/students')
def Students():
    students = [
        {
            "name": "sahil sapariya",
            "age": 20,
            "city": "jamjodhpur",
            "birthdate": '02/11/2003'
        },
        {
            "name": "pranjal javia",
            "age": 20,
            "city": "jamjodhpur",
            "birthdate": '17/12/2003'
        },
        {
            "name": "om kadivar",
            "age": 20,
            "city": "jamjodhpur",
            "birthdate": '21/04/2004'
        }
    ]

    return {
        "message": "Students list with their name, age, city and birthdate",
        "data": students,
        "success": True
    }


if __name__ == "__main__":
    app.run()