from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

@app.route('/user-agent')
def user_agent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/bad')
def bad():
    return '<h1>Bad Request</h1>', 400

if __name__ == '__main__':
    app.run(debug=True)