# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import redis
import json
r = redis.Redis(host='localhost',port=8888,db=0)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("md5store")


def on_message(client, userdata, msg):
    print(msg.topic + " " + ":" + str(msg.payload))
    try:
        code=200
        data = json.loads(msg.payload)
        inputmd5 = data["md5"]
        clientId = data["clientId"]
        result = r.get(inputmd5)
        if result == None:
            print inputmd5 , 'not found'
        else:
            resultjson = json.dumps({'text':result,'code':code})
            client.publish(clientId, resultjson)

    except ValueError:
        return False
    return True




client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("am.appxc.com", 1883, 60)
client.loop_forever()