from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/greet/<name>')
def greet(name):
    return f"hello, {name}!"

@app.route("/about")
def about():
    return "this site is a test for now"

if __name__ == "__main__":
    app.run(debug=True)
    
