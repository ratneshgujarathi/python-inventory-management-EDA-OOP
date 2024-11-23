from pydispatch import dispatcher

class Consumers:
    @staticmethod
    def update_inventory(order_id):
        print(f"Updating inventory for order {order_id}.")

    @staticmethod
    def send_notification(order_id):
        print(f"Sending notification for order {order_id}.")

# Connect consumers to the event
dispatcher.connect(Consumers.update_inventory, signal="order_placed")
dispatcher.connect(Consumers.send_notification, signal="order_placed")
