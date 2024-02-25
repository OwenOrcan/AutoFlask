import os, shutil, sys


def main():
    try:
        if len(sys.argv) < 3 and sys.argv[1] == "init":
            create_flask_structure_folders()
            create_config_file()
            create_routes_file()
            create_flask_run_file()
            print("\033[92mFlask Project Created!\033[0m")
        else:
            print("\033[92mUsage: autoflask init\033[0m")
    except IndexError:
        print("\033[92mUsage: autoflask init\033[0m")


def create_config_file():
    """
    Creates a config.py file with a Flask application configuration.
    """
    content = """
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'YOUR SECRET KEY'

    from routes import routes

    app.register_blueprint(routes, url_prefix="/")

    @app.errorhandler(404)
    def page_not_found(error):
        return "<h1>404 Not Found</h1>", 404

    return app

    """

    with open("config.py", 'w') as file:
        file.write(content.strip())




def create_routes_file():
    """
    Creates a routes.py file with Flask routing using a blueprint.

    """
    content = """
from flask import Blueprint

routes = Blueprint("routes", __name__)


@routes.route("/")
def index():
    return "<h1> Welcome To Your Flask Application! </h1>"

    """
    with open("routes.py", 'w') as file:
        file.write(content.strip())



def create_flask_structure_folders():
    """
    Creates "static" and "templates" folders in the current working directory for a Flask application.
    """
    # Paths for the static and templates folders based on the current working directory
    static_path = os.path.join(os.getcwd(), 'static')
    templates_path = os.path.join(os.getcwd(), 'templates')

    if not os.path.exists(static_path):
        os.makedirs(static_path)
    else:
        shutil.rmtree(static_path)
        os.makedirs(static_path)

    if not os.path.exists(templates_path):
        os.makedirs(templates_path)
    else:
        shutil.rmtree(templates_path)
        os.makedirs(templates_path)


def create_flask_run_file():
    """
    Creates a Python script file that runs a Flask application using the create_app function from the config module.
    """
    content = """
from config import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    """

    with open("app.py", 'w') as file:
        file.write(content.strip())





