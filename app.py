from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_assets import Environment, Bundle
from flask_scss import Scss


app = Flask(__name__)
bootstrap = Bootstrap(app)
scss = Scss(app)



@app.route('/')
def index():
    return render_template("base.html")

@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)

@app.route('/map')
def map():
    return render_template("map.html")

@app.route('/user/map')
def user_map():
    return render_template("user_map.html")

@app.route('/registr')
def registr():
    return render_template('registr.html')

@app.route('/cabinet')
def cabinet():
    return render_template('cabinet.html')

@app.route('/user/cabinet')
def user_cabinet():
    return render_template('user_cabinet.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/user/history')
def user_history():
    return render_template('user_history.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/user/news')
def user_news():
    return render_template('user_news.html')

@app.route('/quarante')
def quarante():
    return render_template('quarante.html')

@app.route('/user/quarante')
def user_quarante():
    return render_template('user_quarante.html')

@app.route('/user/wallets')
def wallets():
    return render_template('wallets.html')

@app.route('/user/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run('0.0.0.0')
