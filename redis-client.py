import redis
import json
from kombu import Exchange, Queue, Message

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Define the message payload
payload = "Hello, Redis queue!"

# Create a Kombu Message object with the payload and required properties
message = Message(
    body=payload,
    delivery_info={
        'exchange': 'celery',
        'routing_key': 'celery'
    },
    properties={
        'correlation_id': 'my_correlation_id',
        'reply_to': 'my_reply_to_queue',
        'delivery_tag': 'my_delivery_tag'
    }
)

# Encode the message as JSON
encoded_message = json.dumps({
    'body': message.body,
    'delivery_info': message.delivery_info,
    'properties': message.properties
})

# Submit the encoded message to the queue 
redis_client.rpush('queue-a10g-1', encoded_message)

print(f"Message '{payload}' submitted to queue 'queue-a10g-1'")