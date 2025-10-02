# save this as app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! Hola"

@app.route("/hello/app/hola")
def hola():
    return "Hola!"

@app.route('/user/<string:username>', methods={'GET'})
def show_user_profile(username):
    print('type(username): ', type(username))
    return'String => {}'.format(username)

@app.route('/user/<int:id>', methods={'GET'})
def show_user_id(id):
    print('type(id): ', type(id))
    return'Int => {}'.format(id)

@app.route('/user/<float:version>', methods={'GET'})
def show_user_version(version):
    print('type(id): ', type(version))
    return'Float => {}'.format(version)

@app.route('/user/test')
def test():
    return '<html><body><h1>TEST<h1></body></html>'

vars = 'Austin_vars'
@app.route('/user/home')
def home():
    return render_template('home.html', text = vars)

@app.route('/user/appinfo')
def AppInfo():
    appInfo={
        'app_id': '314',
        'app_name': ' Flask'
    }
    return render_template('home.html', AppInfo=appInfo)


if __name__ == '__main__':
    app.run('0.0.0.0', debug = True)