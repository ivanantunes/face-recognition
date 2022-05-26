from http.client import BAD_REQUEST, INTERNAL_SERVER_ERROR, OK
from flask import Flask, request
from utils.HttpResponse import HttpResponse
from flask_httpauth import HTTPBasicAuth

class RouterService():
    app = Flask("FaceRecognition")
    auth = HTTPBasicAuth()

    def __init__(self) -> None:
        self.app.run(host="127.0.0.1", port=3000, debug=True)

    @app.route(rule='/auth/login', methods=['POST'])
    def authLogin():
        body = request.get_json()

        if ("username" not in body):
            return HttpResponse(BAD_REQUEST, "Usuário é Obrigatório.")
        
        if ("password" not in body):
            return HttpResponse(BAD_REQUEST, "Senha é Obrigatório.")

        return HttpResponse(INTERNAL_SERVER_ERROR, "Rota Não Implementada")
    
    @app.route(rule='/register/person', methods=['POST'])
    @auth.login_required
    def registerPerson():
        body = request.get_json()

        if ("image" not in body):
            return HttpResponse(BAD_REQUEST, "Imagem é Obrigatório.")
        
        if ("name" not in body):
            return HttpResponse(BAD_REQUEST, "Nome é Obrigatório.")
        
        if ("type" not in body):
            return HttpResponse(BAD_REQUEST, "Tipo é Obrigatório.")

        if (body['type'] != 'P' and body['type'] != 'T'):
            return HttpResponse(BAD_REQUEST, "Tipo Informado Inválido.")
        
        if (body['type'] == 'T' and "start_period" not in body):
            return HttpResponse(BAD_REQUEST, "Período Inicial é Obrigatório")
        
        if (body['type'] == 'T' and "end_period" not in body):
            return HttpResponse(BAD_REQUEST, "Período Final é Obrigatório")

        return HttpResponse(INTERNAL_SERVER_ERROR, "Rota Não Implementada")
    
    @app.route(rule='/register/persons', methods=['POST'])
    @auth.login_required
    def registerPersons():
        body = request.get_json()