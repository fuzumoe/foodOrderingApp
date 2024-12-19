from flask import Response, request, jsonify
from http import HTTPStatus
from flask.views import MethodView
from app.models.order import Order
from app.models.menu_item import MenuItem
from app.models import db


#/orders
class OrderAPI(MethodView):
    def get(self) -> Response:
        orders = Order.query.all()
        data = [
            {
                "id": order.id,
                "customer_name": order.customer_name,
                "items": order.items,
                "total_price": order.total_price
            }
            for order in orders
        ]
        
        return jsonify(data)
    
    def post(self) -> Response:
        data = request.json
        
        customer_name = data["customer_name"]
        # [2, 3, 4, 5]
        item_ids = data["items"] 
        
        # '2', '3', '4', '5' 
        item_ids_str = ",".join(map(str, item_ids))
        # total_price = sum(MenuItem.query.get(item_id).price for item_id in items)
        items = [MenuItem.query.get(item_id)for item_id in item_ids  ]            
        price_of_all_items = [ item.price for item in items]
        total_price = sum(price_of_all_items )
        new_order = Order(customer_name=customer_name, items=item_ids_str, total_price=total_price)
        
        db.session.add(new_order)
        db.session.commit()
        
        response_data = jsonify({"message": "Menu item added successfully"})
        status_code = HTTPStatus.CREATED
        
        return response_data, status_code