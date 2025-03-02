import json
import time

import requests
import os

from fastavro.schema import parse_schema
from pulsar.schema import AvroSchema

PULSAR_ENV: str = 'BROKER_HOST'


def broker_host():
    return os.getenv(PULSAR_ENV, default="localhost")


def consultar_schema_registry(topico: str) -> dict:
    json_registry = requests.get(f'http://{broker_host()}:8080/admin/v2/schemas/public/default/{topico}/schema').json()
    return json.loads(json_registry.get('data', {}))


def obtener_schema_avro_de_diccionario(json_schema: dict) -> AvroSchema:
    definicion_schema = parse_schema(json_schema)
    return AvroSchema(None, schema_definition=definicion_schema)


def time_millis():
    return int(time.time() * 1000)
