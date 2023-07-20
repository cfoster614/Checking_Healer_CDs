from flask import Flask

# from flask_cors import CORS

from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    
    with app.app_context():
        from app.main import bp as main_bp
        from app.models import bp as models_bp
        from app.buckets import bp as buckets_bp
        app.register_blueprint(main_bp)
        app.register_blueprint(models_bp)
        app.register_blueprint(buckets_bp)
        
    return app

  


    
