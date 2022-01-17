import paho.mqtt.client as mqtt
import numpy as np
import time

count = 0
# 0. define callbacks - functions that run when events happen. 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
  print("Connection returned result: "+str(rc))

  # Subscribing in on_connect() means that if we lose the connection and
  # reconnect then subscriptions will be renewed.
  client.subscribe("ece180d/team6/elijah-pub", qos = 1)

# The callback of the client when it disconnects. 
def on_disconnect(client, userdata, rc): 
  if rc != 0: 
    print('Unexpected Disconnect')
  else:
    print('Expected Disconnect')

# The default message callback. 
# (won't be used if only publishing, but can still exist)
def on_message(client, userdata, message): 
  print('Received message: "' + str(message.payload) + '" on topic "' + 
        message.topic + '" with QoS ' + str(message.qos))
  startIndex = int(str(message.payload).find(':'))
  count = int(str(message.payload)[startIndex + 2]) + 1
  #msgLength = len(str(message.payload))
  #count = int(str(message.payload)[msgLength - 2]) + 1
  time.sleep(2)
  client.publish('ece180d/team6/elijah-sub', 'Paging one more time... Total number of messages exchanged: ' + str(count), qos=1)

# 1. create a client instance. 
client = mqtt.Client()
# add additional client options (security, certifications, etc.)
# many default options should be good to start off.
# add callbacks to client. 
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message


# 2. connect to a broker using one of the connect*() functions. 
client.connect_async("test.mosquitto.org")


# 3. call one of the loop*() functions to maintain network traffic flow with the broker. 
client.loop_start()

# 4. use subscribe() to subscribe to a topic and receive messages. 
#client.subscribe("ece180d/team6/elijah-pub")

# 5. use publish() to publish messages to the broker. 
# payload must be a string, bytearray, int, float or None.
print('Publishing...') 
client.publish('ece180d/team6/elijah-sub', 'Can you hear me? Total number of messages exchanged: 1', qos=1)

while True: # perhaps add a stopping condition using some break or something.
  pass # do your non-blocked other stuff here, like receive IMU data or something.
# 6. use disconnect() to disconnect from the broker. 
client.loop_stop()
client.disconnect()