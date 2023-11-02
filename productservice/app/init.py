from flask import Flask
from .routes import product_blueprint

app = Flask(__name__)
app.register_blueprint(product_blueprint)
