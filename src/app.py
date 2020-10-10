from flask import Flask

def create_app():
    app = Flask(__name__)

    from monkey import sp_monkey
    app.register_blueprint(sp_monkey)

    return app
