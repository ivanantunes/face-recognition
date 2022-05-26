import json
from flask import Response

def HttpResponse(status=int, message=str, nameData=False, data=False) -> dict:
    response = {}
    response["status"] = status
    response["message"] = message

    if (nameData and data):
        response[nameData] = data

    return Response(json.dumps(response), status, content_type='application/json')