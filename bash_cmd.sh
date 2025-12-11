#!/bin/bash

set -e  # exit on any failure

BROKER="kafka1:9092"

echo "Creating topics in Kafka KRaft cluster..."

# Create user_logins topic (3 partitions)
docker exec -it kafka1 kafka-topics \
  --create \
  --topic user_logins \
  --partitions 3 \
  --replication-factor 3 \
  --if-not-exists \
  --bootstrap-server $BROKER

# Create user_actions topic (5 partitions)
docker exec -it kafka1 kafka-topics \
  --create \
  --topic user_actions \
  --partitions 5 \
  --replication-factor 3 \
  --if-not-exists \
  --bootstrap-server $BROKER

echo "✔ Topics created successfully!"