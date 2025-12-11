from confluent_kafka import Producer
import uuid, json, random, time

conf = {
    "bootstrap.servers": "localhost:9092,localhost:9094,localhost:9096",
    "acks": "all",
    "enable.idempotence": True,
    "compression.type": "zstd",  # Best compression for big messages
    "retries": 5,
}

producer = Producer(conf)

users = ["101", "102", "103"]
actions = ["click", "scroll", "view", "purchase"]


def delivery_report(err, msg):
    if err:
        print("❌ Failed:", err)
    else:
        print(f"✔ Sent to {msg.topic()} partition {msg.partition()}")

while True:
    user_id = random.choice(users)
    action = random.choice(actions)

    event = {
        "event": "action",
        "action_type": action,
        "user_id": user_id,
        "timestamp": time.time(),
        "event_id": str(uuid.uuid4())
    }

    producer.produce(
        topic="user_actions",
        key=user_id,
        value=json.dumps(event),
        callback=delivery_report
    )

    producer.poll(0)
    print("ACTION EVENT:", event)
    time.sleep(1)
