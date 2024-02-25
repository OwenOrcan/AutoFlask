# AutoFlask

[![asciicast](https://asciinema.org/a/MgPqnItiS0Fj9VCcpq1A1eJWo.svg)](https://asciinema.org/a/MgPqnItiS0Fj9VCcpq1A1eJWo)

AutoFlask is a command-line utility designed to streamline the creation of Flask applications by generating a basic project structure with essential configurations. This tool sets up a Flask project skeleton, allowing developers to jumpstart their Flask application development with best practices in mind.

## Installation

To install AutoFlask, you can use pip:

```bash
pip install autoflask
```

Ensure you have Flask installed in your environment or virtualenv where you plan to run AutoFlask.

## Usage

To create a new Flask application structure, navigate to your project directory in the terminal and run:

```bash
autoflask init
```

This command generates the following project structure:

```
/project
    /static
    /templates
    config.py
    routes.py
    app.py
```

## Generated Project Structure

### `static`

This directory is intended for static files like CSS, JavaScript, and image files. Flask will serve files from this directory under the `/static` endpoint.

### `templates`

The `templates` directory holds your Jinja2 templates. Flask will render these templates when serving pages, allowing for dynamic content generation.

### `config.py`

A configuration file that initializes your Flask app with necessary settings. It includes a placeholder for the secret key and a sample function, `create_app`, to instantiate and configure your Flask application. This file also demonstrates registering a blueprint for your routes and handling a basic 404 error.

#### Example `create_app` function:

```python
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'YOUR SECRET KEY'
    from routes import routes
    app.register_blueprint(routes, url_prefix="/")
    return app
```

### `routes.py`

Defines your Flask routes using a Blueprint. It's a starting point for your application's endpoints.

#### Example route:

```python
from flask import Blueprint

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    return "<h1>Welcome To Your Flask Application!</h1>"
```

### `app.py`

The entry point for running your Flask application. It imports the app from `config.py` and runs the server.

#### Example usage:

```python
from config import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
```

## Contributing

Contributions to AutoFlask are welcome!

## License

[MIT License](LICENSE)

## Acknowledgements

Thank you to the Flask community for providing the inspiration and foundation for building web applications with ease.
