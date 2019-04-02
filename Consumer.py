import pika





connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print("[x] recived%" +str(body))


channel.basic_consume(callback, queue="hello", no_ack=True)
print("waiting for message")

channel.start_consuming()
connection.close()



