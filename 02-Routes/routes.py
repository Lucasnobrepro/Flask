from markupsafe import escape
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

# setando rotas.
def set_routes():
    show_user_profile('lucas_nobre')
    show_post(1)
    show_subpath('into_path')

# Run Hello World.
if __name__ == '__main__':
    app.route(set_routes)

    app.run(debug=True)








