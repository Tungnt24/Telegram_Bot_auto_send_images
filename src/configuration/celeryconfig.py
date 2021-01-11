import os

broker_url = os.getenv("RABBITMQ", "amqp://localhost:5672")
