# Introduction
This project demonstrates a small event-driven system simulating an e-commerce order processing system. It includes:

- Event Producer: Publishes events when an order is placed.
- Event Consumers: Respond to the event (e.g., updating inventory, sending notifications).


## What is event driven architecture?
- **Event-Driven Architecture (EDA)** is a software design pattern where components communicate by producing and responding to events. An event is a significant change in state or occurrence (e.g., user actions, system triggers).

## How It Works (Overview)
- **Event Producers:** Generate events when a state change occurs (e.g., user clicks a button).
- **Event Consumers:** Listen for and respond to events (e.g., processing a payment).
- **Event Channels:** Deliver events from producers to consumers (e.g., message queues).

```
Producer (place_order): Emits the ORDER_PLACED event when an order is placed.
Consumers (update_inventory and send_notification): React to the ORDER_PLACED event.
Dispatcher: Routes the event from the producer to all connected consumers.
```


## Core Components
- Events: Messages describing what happened.
- Event Brokers: Middleware to route events (e.g., Kafka, RabbitMQ).
- Subscribers: Services reacting to specific events.

## Project Structure
```
├── main.py          # Simulates the application
├── events.py        # Defines events and signals
├── consumers.py     # Implements event consumers
```

## How to run the project
1. **Install Dependencies**
```pip install pydispatcher```
OR
```pip install -r requirements.txt```

2. **Place the Order**
Run:
```python main.py 101```

3. **Show the orders placed**
In a separate terminal, run:
```python main.py```

## Extending the Project
- Use Redis Pub/Sub or RabbitMQ for distributed event handling.
- Add more consumers like payment processing or logging.
- Implement asynchronous handling with asyncio or threading.