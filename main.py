import flask
app = flask.Flask(__name__)
 
gloabalObjects = [{'name': 'Test1', 'number': 5342}, {'name': "Test2", 'number': 1112}]


@app.route('/',  methods=['GET', 'POST'])
def hello_world():
    if flask.request.method == 'POST':
        if 'audioUpload' in flask.request.form:
            print("HELLOW PSETER")
            print(flask.request.form['audioUpload'])
        
    context = {}
    context['records'] = gloabalObjects
    return flask.render_template("index.html", **context)

