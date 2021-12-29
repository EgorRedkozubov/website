from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '2jd19487dj2dyjqurewily23fg8c9d'
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app