docker network create kafka-producer-net

docker run -d --name kafka --network kafka-producer-net -e KAFKA_NODE_ID=1 -e KAFKA_PROCESS_ROLES=broker,controller -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:29092,CONTROLLER://0.0.0.0:29093,PLAINTEXT_HOST://0.0.0.0:9092 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka:29092,PLAINTEXT_HOST://localhost:9092 -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@localhost:29093 -e KAFKA_CONTROLLER_LISTENER_NAMES=CONTROLLER -e KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT -e KAFKA_INTER_BROKER_LISTENER_NAME=PLAINTEXT -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 -e KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR=1 -e KAFKA_LOG_DIRS=/tmp/kraft-combined-logs apache/kafka:latest

docker stop producer
docker rm producer
docker rmi messages_producer
docker build -t messages_producer .\producer
docker run --name producer -p 8080:8080 --network kafka-producer-net -d messages_producer


docker network create consumer-mongo

docker run --name mongo_db --network consumer-mongo --hostname=5641c0c0521b --user=mongodb --mac-address=66:d7:fa:3f:60:16 --env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin --env=HOME=/data/db --volume=/data/configdb --volume=/data/db --network=bridge -p 27017:27017 --restart=no --label='description=Container configured with a standalone instance of MongoDB' --label='maintainer=support@mongodb.com' --label='name=MongoDB Standalone' --label='org.opencontainers.image.ref.name=ubuntu' --label='org.opencontainers.image.version=22.04' --label='summary=MongoDB Standalone Container' --label='vendor=MongoDB' --label='version=8.0.12' --runtime=runc -d mongodb/mongodb-community-server:latest

docker stop consumer
docker rm consumer
docker rmi messages_consumer
docker build -t messages_consumer .\consumer-side
docker run --name consumer -p 8081:8080 --network consumer-mongo -d messages_consumer


docker stop mongo_getter
docker rm mongo_getter
docker rmi mongo_messages_getter
docker build -t mongo_messages_getter .\mongo-get-API
docker run --name mongo_getter -p 8082:8080 --network consumer-mongo -d mongo_messages_getter