from app import create_app
from flask import request
import git

app = create_app(debug=False)

@app.route("/git_update", methods=['POST'])
def git_update():
    if request.method == 'POST':
        repo = git.Repo('./sample-flask-app')
        origin = repo.remotes.origin
        repo.create_head('main',
                        origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
        origin.pull()
        return '', 200
    else:
        return '', 400
        
if __name__ == "__main__":
    app.run()