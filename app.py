from flask import Flask, render_template, request, redirect, url_for, app
from joblib import load
from get_comments import get_subreddit_comments, get_predictions


def requestResults(name):
    comments = get_subreddit_comments(name)
    results = get_predictions(comments)
    return comments, results

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('results', name=user))


@app.route('/results/<name>')
def results(name):
    table_html = "<table border='1'>"
    table_html += "<tr><th>Comment</th><th>Prediction</th></tr>"
    comments, results = requestResults(name)
    for comment, prediction in zip(comments,results):
        if prediction == 1:
            table_html += f"<tr style='background-color: #ff6347;'><td>{comment}</td><td>{prediction}</td></tr>"
        else:
            table_html += f"<tr><td>{comment}</td><td>{prediction}</td></tr>"
    table_html += "</table>"
    return table_html


if __name__ == '__main__' :
    app.run(debug=True)