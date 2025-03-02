from flask import Flask

from src.bff.api import ingesta_automatizada


def create_app():
    aplicacion = Flask(__name__)

    aplicacion.debug = True
    aplicacion.register_blueprint(ingesta_automatizada.blueprint)

    @aplicacion.route("/health")
    def health():
        return {"status": "up"}

    return aplicacion
