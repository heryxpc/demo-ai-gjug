import csv
from flask import Flask

app = Flask(__name__)

user_db = [
    { "username": "heryxpc@gmail.com", "password": "password123"},
    { "username": "orlando@gmail.com", "password": "password123"},  
]

@app.route('/')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()

@app.route('/login')
def login(username: str, password: str):
    filename = "users.csv"
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["username"] == username and row["password"] == password:
                return True
    return False
