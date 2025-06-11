from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '허지연바보멍청이뿡☆💨'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

