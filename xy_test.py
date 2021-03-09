""" import numpy as np
def test_return(a,b,c,d):
    return [a,b,c,d]

if __name__ == '__main__':
    my_return = test_return(1,2,33,444)
    print(type(my_return)) """

""" import threading
import time

def read():
    for x in range(5):
        print('在%s,正在听音乐' % time.time())
        time.sleep(1.5)

def write():
    for x in range(5):
        print('在%s,正在看电视' % time.ctime())
        time.sleep(1.5)

def main():

    music_threads = []  # 用来存放执行read函数线程的列表
    TV_threads = []  # 用来存放执行write函数线程的列表

    for i in range(1,2):  # 创建1个线程用于read()，并添加到read_threads列表
        t = threading.Thread(target=read) # 执行的函数如果需要传递参数，threading.Thread(target=函数名,args=(参数，逗号隔开))
        music_threads.append(t)

    for i in range(1,2): # 创建1个线程执行write()，并添加到write_threads列表
        t = threading.Thread(target=write) # 执行的函数如果需要传递参数，threading.Thread(target=函数名,args=(参数，逗号隔开))
        TV_threads.append(t)

    for i in range(0,1):  # 启动存放在read_threads和write_threads列表中的线程
        music_threads[i].start()
        TV_threads[i].start()

if __name__ == '__main__':
    main() """

# python 3.6

import random
import time
import numpy as np
from paho.mqtt import client as mqtt_client
import json

broker = 'broker.emqx.io'
port = 1883
topic = "/python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client,multiobject_track_output):
# while True:
    time.sleep(1)
    msg = multiobject_track_output.tolist()
    msg = json.dumps(msg)
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


def run():
    client = connect_mqtt()
    client.loop_start
    publish(client)


if __name__ == '__main__':
    run()

