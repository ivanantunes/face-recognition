from http.client import BAD_REQUEST, INTERNAL_SERVER_ERROR, OK, UNAUTHORIZED
from flask import Flask, request
from enums.ELog import ELog
from providers.ConfigProvider import ConfigProvider
from providers.DatabaseProvider import DatabaseProvider
from utils.HttpResponse import HttpResponse
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash
import base64
import requests

class RouterService():
    app = Flask("FaceRecognition")
    auth = HTTPBasicAuth()

    def __init__(self) -> None:
        configSys = ConfigProvider().getConfigSystem()
        self.app.run(host="127.0.0.1", port=3000, debug=configSys.DEBUG_MODE)

    @auth.verify_password
    def verifyPassword(username, password):
        configLogin = ConfigProvider().getConfigLogin()

        if configLogin.USERNAME == username and check_password_hash(configLogin.PASSWORD, password):
            return username

    @app.route(rule='/auth/login', methods=['POST'])
    def authLogin():
        body = request.get_json()

        if ("username" not in body):
            return HttpResponse(BAD_REQUEST, "Usuário é Obrigatório.")
        
        if ("password" not in body):
            return HttpResponse(BAD_REQUEST, "Senha é Obrigatório.")

        configLogin = ConfigProvider().getConfigLogin()

        if (body['username'] != configLogin.USERNAME):
            return HttpResponse(UNAUTHORIZED, "Usuário Incorreto.")
        
        if (not check_password_hash(configLogin.PASSWORD, body['password'])):
            return HttpResponse(UNAUTHORIZED, "Senha Incorreta.")

        return HttpResponse(OK, "Login Efetuado com Sucesso.")

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

        pesImage = body['image']
        pesName = body['name']
        pesUuid = None
        pesCard = None
        pesType = body['type']
        pesStartPeriod = None
        pesEndPeriod = None
        pesStatus = 'A'

        if ('status' in body):
            if (body['status'] != 'A' and body['status'] != 'I' and body['status'] != 'B'):
                return HttpResponse(BAD_REQUEST, "Status Inválido,")

        if ('image_url' in body):
            pesImage = base64.b64encode(requests.get(body['image_url']).content)
        
        if ('uuid' in body):
            pesUuid = body['uuid']
        
        if ('card' in body):
            pesCard = body['card']
        
        if ('start_period' in body):
            pesStartPeriod = body['start_period']
        
        if ('end_period' in body):
            pesEndPeriod = body['end_period']

        sql = 'INSERT INTO PERSON(PES_IMG, PES_NAME, PES_UUID, PES_CARD, PES_TYPE, PES_START_PERIOD, PES_END_PERIOD, PES_STATUS) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
        values = (pesImage, pesName, pesUuid, pesCard, pesType, pesStartPeriod, pesEndPeriod, pesStatus)

        database = DatabaseProvider()

        response = database.insert(sql, values)

        if (response.status):
            database.insertLog('[CADASTRO]-[PESSOA]', response.message, ELog.Log_Success)
            return HttpResponse(OK, response.message)
        
        database.insertLog('[CADASTRO]-[PESSOA]', response.response, ELog.Log_Error)
        return HttpResponse(INTERNAL_SERVER_ERROR, response.message, 'error', response.response)
    
    @app.route(rule='/register/persons', methods=['POST'])
    @auth.login_required
    def registerPersons():
        body = request.get_json()

        for row in body:
            if ("image" not in row):
                return HttpResponse(BAD_REQUEST, "Imagem é Obrigatório.")
        
            if ("name" not in row):
                return HttpResponse(BAD_REQUEST, "Nome é Obrigatório.")
            
            if ("type" not in row):
                return HttpResponse(BAD_REQUEST, "Tipo é Obrigatório.")

            if (row['type'] != 'P' and row['type'] != 'T'):
                return HttpResponse(BAD_REQUEST, "Tipo Informado Inválido.")
            
            if (row['type'] == 'T' and "start_period" not in row):
                return HttpResponse(BAD_REQUEST, "Período Inicial é Obrigatório")
            
            if (row['type'] == 'T' and "end_period" not in row):
                return HttpResponse(BAD_REQUEST, "Período Final é Obrigatório")

            pesImage = row['image']
            pesName = row['name']
            pesUuid = None
            pesCard = None
            pesType = row['type']
            pesStartPeriod = None
            pesEndPeriod = None
            pesStatus = 'A'

            if ('status' in row):
                if (row['status'] != 'A' and row['status'] != 'I' and row['status'] != 'B'):
                    return HttpResponse(BAD_REQUEST, "Status Inválido,")

            if ('image_url' in row):
                pesImage = base64.b64encode(requests.get(row['image_url']).content)
            
            if ('uuid' in row):
                pesUuid = row['uuid']
            
            if ('card' in row):
                pesCard = row['card']
            
            if ('start_period' in row):
                pesStartPeriod = row['start_period']
            
            if ('end_period' in row):
                pesEndPeriod = row['end_period']

            sql = 'INSERT INTO PERSON(PES_IMG, PES_NAME, PES_UUID, PES_CARD, PES_TYPE, PES_START_PERIOD, PES_END_PERIOD, PES_STATUS) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
            values = (pesImage, pesName, pesUuid, pesCard, pesType, pesStartPeriod, pesEndPeriod, pesStatus)

            database = DatabaseProvider()

            response = database.insert(sql, values)

            if (not response.status):
                database.insertLog('[CADASTRO]-[PESSOAS]', response.response, ELog.Log_Error)
                return HttpResponse(INTERNAL_SERVER_ERROR, response.message, 'error', response.response)
        
        database.insertLog('[CADASTRO]-[PESSOAS]', response.message, ELog.Log_Success)
        return HttpResponse(OK, "Pessoas Cadastradas com Sucesso.")