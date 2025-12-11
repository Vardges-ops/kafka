@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

echo Creating Kafka topics in KRaft cluster...

REM Broker address inside Docker network
set BROKER=kafka1:9092

echo.
echo Creating topic: user_logins
docker exec -it kafka1 kafka-topics ^
  --create ^
  --topic user_logins ^
  --partitions 3 ^
  --replication-factor 3 ^
  --if-not-exists ^
  --bootstrap-server %BROKER%

echo.
echo Creating topic: user_actions
docker exec -it kafka1 kafka-topics ^
  --create ^
  --topic user_actions ^
  --partitions 5 ^
  --replication-factor 3 ^
  --if-not-exists ^
  --bootstrap-server %BROKER%

echo.
echo ✔ Topics created successfully!

ENDLOCAL
pause