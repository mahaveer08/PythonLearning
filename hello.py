# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print('Successfully running python code')
    return '<html><body><h1>Welcome to Devops!</h1>\n<p><h3>Lets conquer it at the hardest!</h3></p></body></html>'

if __name__ == '__main__':
    app.run()

