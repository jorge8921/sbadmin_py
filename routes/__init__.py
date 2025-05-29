# routes/__init__.py
def register_routes(app):
    from .general import general_bp
    from .dashboard import dashboard_bp
    from .components import components_bp
    from .utilities import utilities_bp
    from .settings import settings_bp
    from .pages import pages_bp

    app.register_blueprint(general_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(components_bp)
    app.register_blueprint(utilities_bp)
    app.register_blueprint(settings_bp)
    app.register_blueprint(pages_bp)