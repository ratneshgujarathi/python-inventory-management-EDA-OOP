import json
from pydispatch import dispatcher

class EventManager:
    ORDER_PLACED = "order_placed"  # Signal name
    ORDER_FILE = "orders.json"  # JSON file to store orders

    def __init__(self):
        self.orders = self.load_orders()

    def load_orders(self):
        """Load orders from the JSON file."""
        try:
            with open(self.ORDER_FILE, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_orders(self):
        """Save orders to the JSON file."""
        with open(self.ORDER_FILE, "w") as file:
            json.dump(self.orders, file)

    def place_order(self, order_id):
        """Emit an order placed event and persist the order."""
        print(f"Event: Order {order_id} placed.")
        self.orders.append(order_id)  # Add to in-memory list
        self.save_orders()  # Persist the updated list
        dispatcher.send(signal=self.ORDER_PLACED, order_id=order_id)

    def show_orders(self):
        """Display all placed orders."""
        print("Orders placed so far:")
        for order in self.orders:
            print(f" - Order ID: {order}")
