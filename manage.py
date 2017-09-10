from flask_script import Manager, Server
from app import app

manager = Manager(app)

@manager.command
def runserver():
	Server(host='localhost', port=8080, debug=True)


if __name__ == "__main__":
	manager.run()