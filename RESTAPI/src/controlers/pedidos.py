from flask import Flask
from flask_restplus import api, resource
from server.instance import server

app, api = server.app, server.api

pedidos_db = [
    {"id": 0, "tittle": 'Pizza Grande'},
    {"id": 1, "tittle": 'Pizza Pequenna'}
]

@api.route("/pedidos")
class List(resource):
    def get(self, ):
        return pedidos_db