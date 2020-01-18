import os
from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

cors = CORS()
app = Flask(__name__)
app.config['SWAGGER'] = {'title': 'Api Documentation', 'uiversion': 2}
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/upload'
app.config.from_object('config')

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

def create_app(debug=False):
    """
    Flask application factory
    Use this function to create new app and use current_app to access
    app related configuration if needed.
    :param debug: boolean
    """

    app.debug = debug

    # register blueprints
    from app.router.compression import mod as compress_route

    app.register_blueprint(compress_route)

    # register extensions
    cors.init_app(app)
    swagger = Swagger(app)


    return app

