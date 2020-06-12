from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

INVENTORY = {
  '1': {'item': 'Laptop bag', 'price': "$23", 'description': 'A 15.6 inch laptop bag'},
  '2': {'item': 'Laptop Charger', 'price': "$20", 'description': 'A 12v laptop charger'},
  '3': {'item': 'Mouse', 'price': "$21", 'description': 'A wireless mouse'},
  '4': {'item': 'Kayboard', 'price': "$22", 'description': 'A mechanical keyboard'},
}
parser = reqparse.RequestParser()

class InventoryList(Resource):
    def get(self):
        return INVENTORY
    def post(self):
        parser.add_argument("item")
        parser.add_argument("price")
        parser.add_argument("description")
        args = parser.parse_args()
        inventory_id = int(max(INVENTORY.keys())) + 1
        inventory_id = '%i' % inventory_id
        INVENTORY[inventory_id] = {
            "item": args["item"],
            "price": args["price"],
            "description": args["description"],
        }
        return INVENTORY[inventory_id], 201

class Inventory(Resource):
  def get(self, inventory_id):
    if inventory_id not in INVENTORY:
     return "Not found", 404
    else:
      return INVENTORY[inventory_id]
  def put(self, inventory_id):
    parser.add_argument("item")
    parser.add_argument("price")
    parser.add_argument("description")
    args = parser.parse_args()
    if inventory_id not in INVENTORY:
      return "Record not found", 404
    else:
      inventory = INVENTORY[inventory_id]
      inventory["item"] = args["item"] if args["item"] is not None else inventory["item"]
      inventory["price"] = args["price"] if args["price"] is not None else inventory["price"]
      inventory["description"] = args["description"] if args["description"] is not None else inventory["description"]
      return inventory, 200

  def delete(self, inventory_id):
    if inventory_id not in INVENTORY:
      return "Not found", 404
    else:
      del INVENTORY[inventory_id]
      return '', 204
api.add_resource(InventoryList, '/')
api.add_resource(Inventory, '/<inventory_id>')
if __name__ == "__main__":
  app.run(debug=True)
