from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Habilitar CORS para toda la aplicación
CORS(app)  # Permite solicitudes desde cualquier origen


from models import Item


# Ejemplo de endpoint para obtener todos los elementos
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])


# Ejemplo de endpoint para agregar un nuevo elemento
@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    new_item = Item(name=data['name'], description=data['description'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201