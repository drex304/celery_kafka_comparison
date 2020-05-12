# celery_kafka_comparison
A simple comparison of vanilla celery and kafka comparison


# Installs

### Virtual environment
```
mkvirtualenv --python-which python3 ckc
```

### Install python packages
```
pip install celery
pip install pykafka
```

### Install rabbitmq
```
sudo apt-get install rabbitmq-server
```
### Install Kafka
Download the 2.5.0 release and un-tar it.  Examples in https://kafka.apache.org/quickstart
```
tar -xzf kafka_2.12-2.5.0.tgz
cd kafka_2.12-2.5.0
```

# Running the Kafka Demo
#### start zookeeper in a terminal within the kafka_2.12-2.5.0 folder
```
bin/zookeeper-server-start.sh config/zookeeper.properties 
```

#### Start Kafka Server in a terminal within the kafka_2.12-2.5.0 folder
```
bin/kafka-server-start.sh config/server.properties
```

#### Create a test topic from within the kafka_2.12-2.5.0 folder
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 6 --topic test

#### Start the Kafka Producer
In the kafka folder
```
python demo_producer.py
```
#### Start Kafka Consumer
In the kafka folder
```
python demo_consumer.py
```

# Running the Celery Demo

#### Running Celery Worker
In the celery folder, start a cerlery worker
```
celery -A demo_consumer worker --loglevel=warn
```

#### Running Celery Producer
In the celery folder, run the celery consumer
```
python demo_producer
```

