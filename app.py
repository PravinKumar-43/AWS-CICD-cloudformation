from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>Simple Calculator</h2>

    <h3>Add and Subtract</h3>
    <form action="/calculate">
        Number 1: <input name="a"><br>
        Number 2: <input name="b"><br><br>

        <button type="submit" name="op" value="add">Add</button>
        <button type="submit" name="op" value="sub">Subtract</button>
    </form>
    '''

@app.route('/calculate')
def calculate():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    op = request.args.get('op')

    if op == "add":
        result = a + b
    elif op == "sub":
        result = a - b

    return f"<h3>Result: {result}</h3>"

app.run(host="0.0.0.0", port=5000)
