from xmlrpc.client import Boolean


class DatabaseResponse():
    def __init__(self, status=bool, message=str, response=None) -> None:
        self.status = status
        self.message = message
        self.response = response