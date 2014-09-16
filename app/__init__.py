from flask.ext.sqlalchemy import SQLAlchemy
import os
db = SQLAlchemy()

def create_app():
    from flask import Flask
    from .api_1_0 import api_blueprint as api_1_0_blueprint
    from .api_1_0 import api
    app = Flask(__name__)
    app.register_blueprint(api_1_0_blueprint)
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql://' + os.environ.get('DB_USER') + \
        ':' + os.environ.get('DB_PASS') + \
        '@' + os.environ.get('DB_HOST') + \
        '/' + os.environ.get('DB')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    db.init_app(app)
    api.init_app(app)
    return app