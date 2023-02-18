from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route('/')
def  hello_world():
    print('Welcome to the main page')
    return 'Hello, World!'


@home_routes.route('/about')
def  about():
    print('We are now in the about page')
    return 'About Me (TODO)'