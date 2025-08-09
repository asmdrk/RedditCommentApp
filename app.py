from flask import Flask, render_template, request, redirect, url_for, app
from joblib import load
from get_comments import get_subreddit_comments


def requestResults(name):
    results = get_subreddit_comments(name)
    return results

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', name=user))


@app.route('/success/<subreddit>')
def success(name):
    return "<xmp>" + str(requestResults(name)) + " </xmp> "


if __name__ == '__main__' :
    app.run(debug=True)