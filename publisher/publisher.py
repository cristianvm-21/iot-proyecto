import json
import random
import time

import paho.mqtt.client as mqtt


BROKER = "emqx"
PORT = 1883
TOPIC = "iot/ta3/dht22"


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)


while True:
    try:
        print(f"Intentando conectar a {BROKER}:{PORT}...")

        client.connect(BROKER, PORT, 60)

        print("Conexion exitosa a EMQX")
        break

    except ConnectionRefusedError:
        print("EMQX aun no esta disponible. Reintentando en 3 segundos...")
        time.sleep(3)


client.loop_start()


while True:

    temperatura = round(random.uniform(20, 35), 2)
    humedad = round(random.uniform(40, 80), 2)

    payload = {
        "temperatura": temperatura,
        "humedad": humedad
    }

    mensaje = json.dumps(payload)

    result = client.publish(
        TOPIC,
        mensaje,
        qos=0,
        retain=False
    )

    print(f"Publicado en {TOPIC}: {mensaje}")

    time.sleep(10)