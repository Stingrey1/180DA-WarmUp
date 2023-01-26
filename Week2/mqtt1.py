import paho.mqtt.client as mqtt

counter = 0

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("your_topic")

def on_message(client, userdata, msg):
    global counter
    counter += 1
    print("Received message. Counter:", counter)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("your_broker_host", 1883, 60)
client.loop_forever()
