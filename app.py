from flask import Flask

app = Flask(__name__)

@app.route('/')
def who():
    return 'Hi my name is Amir'