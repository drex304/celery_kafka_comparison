from demo_consumer import process
import uuid
import time

INTERVAL = 5  # seconds
message_count = 0
output_iteration = 0
start_time = time.time()

while True:
    identifier = str(uuid.uuid4())
    r = process.delay(message=identifier)
    message_count += 1
    now = time.time()

    if (now - start_time) > INTERVAL:
        print('{}) {} messages produced at {:.4f} Hz'.format(
            output_iteration,
            message_count,
            message_count / (now - start_time)
        ))
        print('', flush=True)
        output_iteration += 1
        message_count = 0
        start_time = time.time()
