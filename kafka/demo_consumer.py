from pykafka import KafkaClient
import time
import uuid
import os

COMSUMER_GROUP="test_group"
TOPIC = 'test'
KAFKA_HOSTS = ['localhost:9092']
ZOOKEEPER_HOSTS = ['localhost:2181']
INTERVAL = 5  # seconds
pid = os.getpid()

kafka_client = KafkaClient(hosts=','.join(KAFKA_HOSTS))
topic = kafka_client.topics[TOPIC]

# simple or balanced consumer, balanced will balance themselves across the consumers
consumer = topic.get_balanced_consumer(
    consumer_group=COMSUMER_GROUP,
    zookeeper_connect=','.join(ZOOKEEPER_HOSTS),
)

output_iteration = 0
message_count = 0
partitions = set()
start_time = time.time()

while True:
    message = consumer.consume()
    identifier = uuid.UUID(message.value.decode('utf-8'))
    partitions.add(message.partition.id)
    message_count += 1
    now = time.time()
    if (now - start_time) > INTERVAL:
        print('{}: {}) {} messages consumed at {:.4f} Hz'.format(
            pid,
            output_iteration,
            message_count,
            message_count / (now - start_time)
        ))
        print('{}: last offset {}, partitions: {}'.format(pid, message.offset, sorted(partitions)))
        print('', flush=True)
        output_iteration += 1
        message_count = 0
        partitions = set()
        start_time = time.time()
