from pykafka import KafkaClient
import time
import uuid
import os

TOPIC = 'test'
KAFKA_HOSTS = ['localhost:9092']
ZOOKEEPER_HOSTS = ['localhost:2181']
INTERVAL = 5  # seconds
pid = os.getpid()

kafka_client = KafkaClient(hosts=','.join(KAFKA_HOSTS))
topic = kafka_client.topics[TOPIC]

with topic.get_producer() as producer:
    output_iteration = 0
    message_count = 0
    start_time = time.time()
    while True:
        identifier = str(uuid.uuid4())
        producer.produce(identifier.encode('utf-8'))
        message_count += 1
        now = time.time()

        if (now - start_time) > INTERVAL:
            print('{}: {}) {} messages produced at {:.4f} Hz'.format(
                pid,
                output_iteration,
                message_count,
                message_count / (now - start_time)
            ))
            print('', flush=True)
            output_iteration += 1
            message_count = 0
            start_time = time.time()


