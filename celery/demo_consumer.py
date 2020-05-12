from celery import Celery
import time
import uuid

# Create the app and set the broker location (RabbitMQ)
app = Celery('Test',
             backend='rpc://',
             broker='pyamqp://guest@localhost//')


def timeit(method):
    def timed(*args, **kwargs):
        interval = 5  # seconds
        result = method(*args, **kwargs)
        now = time.time()
        timed.message_count += 1
        if (now - timed.start_time) > interval:
            print('{}) {} messages consumed at {:.4f} Hz'.format(
                timed.output_interval,
                timed.message_count,
                timed.message_count / (now - timed.start_time)
            ))
            timed.start_time = time.time()
            timed.output_interval += 1
        return result
    timed.start_time = time.time()
    timed.output_interval = 0
    timed.message_count = 0
    return timed


@app.task
@timeit
def process(message):
    _ = uuid.UUID(message)
