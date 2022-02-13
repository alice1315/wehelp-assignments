from flask import Flask

def create_app():
    app = Flask(__name__, static_folder = "static", static_url_path = "/")

    from .home import home as home_blueprint
    from .auth import auth as auth_blueprint
    from .member import member as member_blueprint

    app.register_blueprint(home_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(member_blueprint, url_prefix = "/member/")

    app.config.from_pyfile("config.py")
    app.secret_key = app.config.get("SECRET_KEY")
    
    return app
