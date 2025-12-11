from confluent_kafka import Consumer, KafkaException
import json

conf = {
    "bootstrap.servers": "localhost:9092,localhost:9094,localhost:9096",
    "group.id": "analytics_group",
    "auto.offset.reset": "earliest",   # Start from beginning if no commits
    "enable.auto.commit": True,
}

consumer = Consumer(conf)

consumer.subscribe(["user_logins", "user_actions"])

print("📡 Consumer started. Listening on topics...")

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())

        event = json.loads(msg.value().decode("utf-8"))
        print(
            f"📥 Topic={msg.topic()} | "
            f"Partition={msg.partition()} | "
            f"Offset={msg.offset()} → {event}"
        )
except Exception as e:
    print(f"Critical exception {e}")
finally:
    consumer.close()