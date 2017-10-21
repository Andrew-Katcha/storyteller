import flask
import os 
from werkzeug.utils import secure_filename


dir_path = os.path.dirname(os.path.realpath(__file__))
app = flask.Flask(__name__)
 
gloabalObjects = [{'name': 'Test1', 'number': 5342}, {'name': "Test2", 'number': 1112}]
app.config['UPLOAD_FOLDER'] = dir_path


@app.route('/',  methods=['GET', 'POST'])
def hello_world():
    if flask.request.method == 'POST':
        if 'audioUpload' in flask.request.form:
            print(flask.request.files)
            print("HELLOW PSETER")
            f = flask.request.files['audioUpload']
            print(f.save(secure_filename(f.filename)))
        
    context = {}
    context['records'] = gloabalObjects
    return flask.render_template("index.html", **context)

