from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
	return "Hello"


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

# @app.errorhandler(DatabaseError)
# def special_exception_handler(error):
#     return 'Database connection failed', 500


app.run()