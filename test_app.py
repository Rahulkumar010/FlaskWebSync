from flask import Flask
from markupsafe import escape
import git

app = Flask(__name__)


@app.route("/git_update", methods=['POST'])
def git_update():
    repo = git.Repo('./sample-flask-app')
    origin = repo.remotes.origin
    repo.create_head('main',
                     origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200


@app.route("/")
def home():
    return "Hello World!"


@app.route("/<name>")
def hello(name):
    return f"Hello {escape(name)}!!, Welcome to Sample Flask Application"

if __name__=="__main__":
    app.run()
