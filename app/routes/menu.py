from flask import Response, request, jsonify
from http import HTTPStatus
from flask.views import MethodView
from app.models.menu_item import MenuItem
from app.models import db

# /menu_items ...
class MenuAPI(MethodView):
    def get(self) -> Response:
        menu_items = MenuItem.query.all()
        data =[
            {
                "id": item.id,
                "name": item.name,
                "price": item.price
            }
            for item in menu_items
        ]
        return jsonify(data)
    
    def post(self) -> Response:
        data = request.json 
        new_item = MenuItem(name=data['name'], price=data['price'])
        
        db.session.add(new_item)
        db.session.commit()
        
        response_data = jsonify({"message": "Menu item added successfully"})
        status_code = HTTPStatus.CREATED
        
        return response_data, status_code