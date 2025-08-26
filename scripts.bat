docker network create kafka-producer-net

docker run --name kafka --network kafka-producer-net --hostname=1ef2ab959c60 --user=appuser --mac-address=4e:ab:89:54:28:fb --env=PATH=/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin --env=JAVA_HOME=/opt/java/openjdk --env=LANG=en_US.UTF-8 --env=LANGUAGE=en_US:en --env=LC_ALL=en_US.UTF-8 --env=JAVA_VERSION=jdk-21.0.6+7 --volume=/etc/kafka/secrets --volume=/mnt/shared/config --volume=/var/lib/kafka/data --network=bridge --workdir=/ --restart=no --label='maintainer=Apache Kafka' --label='org.label-schema.build-date=2025-03-14' --label='org.label-schema.description=Apache Kafka' --label='org.label-schema.name=kafka' --label='org.label-schema.vcs-url=https://github.com/apache/kafka' --runtime=runc -d apache/kafka:latest


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