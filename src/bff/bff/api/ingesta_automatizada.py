import os
import uuid

import requests
from flask import Blueprint, request

from src.bff import utils
from src.bff.despachadores import Despachador

blueprint = Blueprint('ingesta_automatizada', __name__, url_prefix="/bff/ingesta_automatizada")

STA_HOST = os.getenv("STA_HOST", default="localhost")


@blueprint.route('/imagen_medica', methods=['POST'])
def agregar_imagen_medica():
    comando = dict(
        id=str(uuid.uuid4()),
        time=utils.time_millis(),
        specversion="v1",
        type="ComandoImagenMedica",
        ingestion=utils.time_millis(),
        datacontenttype="AVRO",
        service_name="BFF",
        data=request.json
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comandos-imagen-medica")
    return [{'message': 'Su imagen esta siendo agregada'}], 203


@blueprint.route('/imagen_medica/<id>', methods=['GET'])
def dar_imagen_medica(id=None):
    return requests.get(f'http://{STA_HOST}:5000/ingesta_automatizada/imagen_medica-query/{id}').json()
