import paho.mqtt.client as mqtt


def test():
    client = mqtt.Client()
    client.connect("127.0.0.1", 1883)
    client.publish("topic1", "mqtt pub test")


if __name__ == '__main__':
    test()
