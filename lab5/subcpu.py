import paho.mqtt.client as mqtt
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("MyCPU")
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode()))
#client = mqtt.Client()
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
#client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
#client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()
