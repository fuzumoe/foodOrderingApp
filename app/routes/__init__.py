from flask import Blueprint
from flask_restx import Api 
from .menu import MenuAPI
from .order import OrderAPI


def register_routes(api: Api) -> None: 
    # Create namespaces for organizing routes
    menu_ns = api.namespace('menu', description='Menu related operations')
    order_ns = api.namespace('order', description='Order related operations')
        
    # menu_blueprint =  Blueprint('menu', __name__)
    # order_blueprint = Blueprint('order', __name__)
    
    menu_ns.add_resource(MenuAPI, '/menu', methods=['GET','POST'])
    order_ns.add_resource(OrderAPI, '/orders', methods=['GET'])
    order_ns.add_resource(OrderAPI, '/order', methods=['POST'])
    
    
    # menu_blueprint.add_url_rule("/menu", view_func=MenuAPI.as_view('menu_api'), methods=['GET','POST'])
    # order_blueprint.add_url_rule("/order", view_func=OrderAPI.as_view('order_list_api'), methods=['POST'])
    # order_blueprint.add_url_rule("/orders", view_func=OrderAPI.as_view('order_create_api'), methods=['GET'])
    
    
    api.add_namespace(menu_ns)
    api.add_namespace(order_ns)


    # app.register_blueprint(menu_blueprint)
    # app.register_blueprint(order_blueprint)