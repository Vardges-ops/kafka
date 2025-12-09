import json
from time import sleep

from confluent_kafka import Consumer


consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    "group.id": "my-group",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)

consumer.subscribe(["orders"])
try:
    while True:
        msg = consumer.poll()
        if msg is None:
            sleep(10)
        elif msg.error():
            print(f"Error while polling {msg.error()}")
        else:
            msg_value = msg.value().decode("utf-8")
            data = json.loads(msg_value)
            print(f"Polled data {data}")
except Exception as e:
    print("Closing the connection and axit the program")
finally:
    consumer.close()