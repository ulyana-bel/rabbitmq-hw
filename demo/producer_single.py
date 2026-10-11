import pika

from settings import URI

# params = pika.ConnectionParameters('localhost')
params = pika.URLParameters(URI)
conn = pika.BlockingConnection(params)
channel = conn.channel()

channel.queue_declare(queue="que_hw_ulyana_bel")

if __name__ == "__main__":

    channel.basic_publish(
        exchange="",
        routing_key="que_hw_ulyana_bel",
        body="Hello, SYSDB-59! - 8.10.2026",
    )
