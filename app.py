import flask 
from flask import request

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def index():
    return "<h1>Meu ChuChu</h1>"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
