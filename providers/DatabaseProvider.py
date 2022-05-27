import sqlite3
from enums.ELog import ELog
from models.Database import DatabaseResponse
from .ConfigProvider import ConfigProvider
from utils.PrintLog import PrintLog

class DatabaseProvider():
    __pathDatabase = 'face_recognition.db'
    __configSys = ConfigProvider().getConfigSystem()

    def __init__(self) -> None:
        
        if self.__configSys.DEV_MODE:
            self.__pathDatabase = '_developer/face_recognition.db'

    def getConnection(self):
        conn = sqlite3.connect(self.__pathDatabase)
        conn.row_factory = sqlite3.Row
        return conn

    def migrations(self) -> None:
        with open('migrations/migration_001.sql') as migration_001:
            print("Executando migration_001")
            self.getConnection().executescript(migration_001.read())
            print("Executado com Sucesso.")

    
    def insert(self, sql=str, values=()):
        connection = self.getConnection()
        cursor = connection.cursor()

        try:
            cursor.execute(sql, values)
            connection.commit()
            connection.close()
            return DatabaseResponse(True, 'Inserção Realizada com Sucesso.')
        except Exception as error:
            connection.rollback()
            connection.close()
            return DatabaseResponse(False, 'Falha ao Executar Inserção. Rollback Efetuado.', error)

    def update(self, sql=str, values=()):
        connection = self.getConnection()
        cursor = connection.cursor()

        try:
            cursor.execute(sql, values)
            connection.commit()
            connection.close()
            return DatabaseResponse(True, 'Atualização Realizada com Sucesso.')
        except Exception as error:
            connection.rollback()
            connection.close()
            return DatabaseResponse(False, 'Falha ao Executar Atualização. Rollback Efetuado.', error)

    def delete(self, sql=str, values=()):
        connection = self.getConnection()
        cursor = connection.cursor()

        try:
            cursor.execute(sql, values)
            connection.commit()
            connection.close()
            return DatabaseResponse(True, 'Exclusão Realizada com Sucesso.')
        except Exception as error:
            connection.rollback()
            connection.close()
            return DatabaseResponse(False, 'Falha ao Executar Exclusão. Rollback Efetuado.', error)

    def getData(self, sql=str, values=()):
        connection = self.getConnection()
        
        try:
            rows = connection.execute(sql, values).fetchall()
            connection.close()
            return DatabaseResponse(True, 'Consulta Realizada com Sucesso.', rows)
        except Exception as error:
            connection.close()
            return DatabaseResponse(False, 'Falha ao Executar Consulta.', error)
    
    def insertLog(self, description=str, message='', status=ELog):
        connection = self.getConnection()
        cursor = connection.cursor()

        try:
            if (self.__configSys.DEV_MODE == False or self.__configSys.DEBUG_MODE == False and status == ELog.Log_Developer or status == ELog.Log_Success):
                PrintLog(description, message, str(status.value))
                return DatabaseResponse(True, 'Log Criado com Sucesso.')
            
            cursor.execute('INSERT INTO LOG(LOG_DESCRIPTION, LOG_MESSAGE, LOG_STATUS) VALUES(?, ?, ?)', (description, message, str(status.value)))
            connection.commit()
            connection.close()

            PrintLog(description, message, str(status.value))

            return DatabaseResponse(True, 'Log Criado com Sucesso.')
        except Exception as error:
            connection.rollback()
            connection.close()
            return DatabaseResponse(False, 'Falha ao Criar Log. Rollback Efetuado.', error)