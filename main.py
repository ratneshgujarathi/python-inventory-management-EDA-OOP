import sys
from event_manager import EventManager
import consumers  # Ensure consumers are loaded and connected

if __name__ == "__main__":
    manager = EventManager()

    if len(sys.argv) > 1:
        order_id = int(sys.argv[1])
        manager.place_order(order_id)
    else:
        print("No order ID provided. Showing all orders:")
        manager.show_orders()
