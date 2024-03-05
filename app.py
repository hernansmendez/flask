from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '¡Educación IT - Docker FlaskApp!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)