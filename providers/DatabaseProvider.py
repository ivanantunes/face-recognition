import sqlite3

from models.Database import DatabaseResponse

class DatabaseProvider():
    __pathDatabase = 'face_recognition.db'

    def __init__(self) -> None:
        pass
    
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

