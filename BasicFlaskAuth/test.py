from flask import Flask, request

app = Flask(__name__)


@app.route('/headers')
def headers():
    # @TODO unpack the request header
    auth = request.headers.get('Authorization', None)

    print(auth)
    return 'not implemented'
