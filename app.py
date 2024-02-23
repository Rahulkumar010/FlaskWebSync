from flask import Flask, render_template
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
    return '',200

@app.route("/")
def index():
    return "Hello World!"

@app.route("/<name>")
def hello(name):
    return f"Hello {escape(name)}!!"

if __name__=="__main__":
    app.run()