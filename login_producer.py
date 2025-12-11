from confluent_kafka import Producer
import uuid, json, random, time

conf = {
    "bootstrap.servers": "localhost:9092,localhost:9094,localhost:9096",
    "acks": "all",                      # Strong durability
    "enable.idempotence": True,         # Exactly-once (producer side)
    "compression.type": "lz4",          # Faster, smaller messages
}

producer = Producer(conf)

users = ["101", "102", "103"]


def delivery_report(err, msg):
    if err is not None:
        print("Delivery failed:", err)
    else:
        print(f"Delivered to {msg.topic()} [{msg.partition()}] @ offset {msg.offset()}")


while True:
    user_id = random.choice(users)

    event = {
        "event": "login",
        "user_id": user_id,
        "timestamp": time.time(),
        "event_id": str(uuid.uuid4())
    }

    producer.produce(
        topic="user_logins",
        key=user_id,
        value=json.dumps(event),
        callback=delivery_report
    )

    producer.flush()   # triggers callbacks
    print("LOGIN EVENT:", event)
    time.sleep(1)