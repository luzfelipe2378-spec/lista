from flask import Flask, jsonify

app = Flask(__name__)

pessoas = [
    {'nome': 'Ana', 'idade': 25, 'cidade': 'SP'},
    {'nome': 'Bruno', 'idade': 30, 'cidade': 'RJ'},
    {'nome': 'Carlos', 'idade': 22, 'cidade': 'MG'}
]

@app.route('/lista')
def lista():
    return jsonify(pessoas)

if __name__ == '__main__':
    app.run(debug=True)
