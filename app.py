from flask import Flask
from service.routes import bp as product_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(product_routes)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
