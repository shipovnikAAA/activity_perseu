from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_mapping({
    'DEBUG': True,
    'SECRET_KEY': 'dev',
    # 'SQLALCHEMY_DATABASE_URI': 'sqlite:///mydatabase.db'
})

    from . import routes
    app.register_blueprint(routes.bp)

    return app