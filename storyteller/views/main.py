from flask import Flask
#import storyteller
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    context = {}
    record0 = {}
    record1 = {}
    record0['name'] = "Hi peter"
    record1['name'] = "Hi andrew"
    context['records'].append(record0)
    context['records'].append(record1)
    return flask.render_template("index.html", **context)
