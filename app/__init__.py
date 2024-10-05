from flask import Flask

def create_app():

    app = Flask(__name__)

    # Import and register Blueprints
    from .main.views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from ..neo.views import neo as neo_blueprint
    app.register_blueprint(neo_blueprint, url_prefix = '/asteroids')

    from ..simulation.views import simulation as simulation_blueprint
    app.register_blueprint(simulation_blueprint,url_prefix='/simulate')

    from ..community.views import community as commmunity_blueprint
    app.register_blueprint(commmunity_blueprint, url_prefix='/community')

    return app