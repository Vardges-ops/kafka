import json
import uuid

from confluent_kafka import Producer

def callback_report(err, msg):
    if err:
        print(f"message failed: {err}")
    else:
        print(f"message succeeded {msg.value().decode("utf-8")}")
        print(f"message info {msg.topic()}, {msg.partition()}, {msg.offset()}")

producer_config = {'bootstrap.servers': 'localhost:9092'}

producer = Producer(producer_config)

order = {
    "order_id": str(uuid.uuid4()),
    "user": "John",
    "item": "items group 1",
}

value = json.dumps(order).encode("utf-8")

producer.produce(topic="orders", value=value, callback=callback_report)

producer.flush()