docker network create kafka-producer-net

docker run --name kafka --network kafka-producer-net --hostname=1ef2ab959c60 --user=appuser --mac-address=4e:ab:89:54:28:fb --env=PATH=/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin --env=JAVA_HOME=/opt/java/openjdk --env=LANG=en_US.UTF-8 --env=LANGUAGE=en_US:en --env=LC_ALL=en_US.UTF-8 --env=JAVA_VERSION=jdk-21.0.6+7 --volume=/etc/kafka/secrets --volume=/mnt/shared/config --volume=/var/lib/kafka/data --network=bridge --workdir=/ -p 9092:9092 --restart=no --label='maintainer=Apache Kafka' --label='org.label-schema.build-date=2025-03-14' --label='org.label-schema.description=Apache Kafka' --label='org.label-schema.name=kafka' --label='org.label-schema.vcs-url=https://github.com/apache/kafka' --runtime=runc -d apache/kafka:latest


docker stop producer
docker rm producer
docker rmi messages_producer
docker build -t messages_producer .\producer
docker run --name producer -p 8081:8080 --network kafka-producer-net -d messages_producer


docker build -t messages_consumer .\consumer-side
docker build -t messages_mongo_getter .\mongo-get-API

