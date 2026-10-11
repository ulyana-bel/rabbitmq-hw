import pika

from settings import URI

# params = pika.ConnectionParameters('localhost')
params = pika.URLParameters(URI)
conn = pika.BlockingConnection(params)
channel = conn.channel()

channel.queue_declare(queue="que_hw_ulyana_bel")

if __name__ == "__main__":

    #count = 0

    #while True:
    #    channel.basic_publish(
    #        exchange="",
    #        routing_key="que_hw_ulyana_bel",
    #        body=f"Hello, SYSDB-59! - {count}",
    #    )
    #    count += 1
 
     # Вместо while True используем range
    for count in range(1000):
        channel.basic_publish(
            exchange="",
            routing_key="que_hw_ulyana_bel",
            body=f"Hello, SYSDB-59! - {count}",
        )
    
    
    print("Отправлено 1000 сообщений. Работа завершена.")
