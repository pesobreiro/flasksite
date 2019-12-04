"""
This script runs the flasksite application using a development server.

We are testing the creation of the forms

"""

from os import environ
from flasksite import app
from flask_images import Images

app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['RECAPTCHA_PUBLIC_KEY'] = 'iubhiukfgjbkhfvgkdfm'
app.config['RECAPTCHA_PARAMETERS'] = {'size': '100%'}
app.debug = True

images = Images(app)


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
