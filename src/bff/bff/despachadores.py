import pulsar

from src.bff import utils


class Despachador():
    def __init__(self):
        ...

    def publicar_mensaje(self, mensaje, topico):
        json_schema = utils.consultar_schema_registry(topico)
        avro_schema = utils.obtener_schema_avro_de_diccionario(json_schema)

        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=avro_schema)
        publicador.send(mensaje)
        cliente.close()
