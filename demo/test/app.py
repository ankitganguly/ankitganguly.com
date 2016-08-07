from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login-submission', methods=( "POST"))
def login():
    print request.args
    print request.form
    return jsonify(request.args)

app.run(debug=True)
