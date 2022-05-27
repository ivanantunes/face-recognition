from enums.ELog import ELog
from datetime import datetime

def PrintLog(description=str, message=None, status=str):
    dateTime = datetime.now()
    dateTime = dateTime.strftime("%d/%m/%Y %H:%M:%S")
    dateTime = '[' + dateTime + ']'

    if (message == None):
        message = ''

    print(dateTime + ' - [' + status + ']: ' + description + '\n' + message)
