from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print("Hello Sasi")
    return "Hello Sasi"

if __name__ == '__main__':
    app.run()
