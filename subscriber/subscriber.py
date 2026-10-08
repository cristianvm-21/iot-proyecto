import json
import os
import time

import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS


# -------------------------
# MQTT
# -------------------------

MQTT_BROKER = "emqx"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/ta3/dht22"


# -------------------------
# InfluxDB
# -------------------------

INFLUX_URL = "http://influxdb:8086"
INFLUX_ORG = os.getenv("INFLUX_ORG")
INFLUX_BUCKET = os.getenv("INFLUX_BUCKET")
INFLUX_TOKEN = os.getenv("INFLUX_TOKEN")


influx_client = InfluxDBClient(
    url=INFLUX_URL,
    token=INFLUX_TOKEN,
    org=INFLUX_ORG
)

write_api = influx_client.write_api(
    write_options=SYNCHRONOUS
)


def on_connect(client, userdata, flags, reason_code, properties):

    print(f"Conectado a EMQX. Codigo: {reason_code}")

    client.subscribe(MQTT_TOPIC)

    print(f"Suscrito a: {MQTT_TOPIC}")


def on_message(client, userdata, message):

    try:

        payload = message.payload.decode("utf-8")

        print(f"Mensaje recibido: {payload}")

        data = json.loads(payload)

        temperatura = data["temperatura"]
        humedad = data["humedad"]

        point = (
            Point("dht22")
            .field("temperatura", float(temperatura))
            .field("humedad", float(humedad))
        )

        write_api.write(
            bucket=INFLUX_BUCKET,
            org=INFLUX_ORG,
            record=point
        )

        print(
            f"Guardado en InfluxDB: "
            f"temperatura={temperatura}, "
            f"humedad={humedad}"
        )

    except Exception as error:

        print(f"Error procesando mensaje: {error}")


mqtt_client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message


while True:

    try:

        print(
            f"Intentando conectar a EMQX "
            f"{MQTT_BROKER}:{MQTT_PORT}..."
        )

        mqtt_client.connect(
            MQTT_BROKER,
            MQTT_PORT,
            60
        )

        break

    except ConnectionRefusedError:

        print(
            "EMQX no disponible. "
            "Reintentando en 3 segundos..."
        )

        time.sleep(3)


mqtt_client.loop_forever()