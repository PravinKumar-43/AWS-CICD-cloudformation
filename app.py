from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>Simple Calculator</h2>
    <form action="/add","/sub">
        Number 1: <input name="a"><br>
        Number 2: <input name="b"><br>
        <input type="submit" value="Add","Subtract">
    </form>
    '''

@app.route('/add')
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"<h3>Result: {a+b}</h3>"

@app.route('/sub')
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"<h3>Result: {a-b}</h3>"

app.run(host="0.0.0.0", port=5000)
