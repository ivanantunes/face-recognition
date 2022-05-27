from enums.ELog import ELog
from services.RouterService import RouterService
from providers.DatabaseProvider import DatabaseProvider

RouterService().startRouters()
# database = DatabaseProvider()

# database.migrations()
# response = database.insert('INSERT INTO LOG(LOG_DESCRIPTION, LOG_STATUS) VALUES(?, ?)', ('Teste de Banco 2', 'DEV'))
# response = database.insert("UPDATE LOG SET LOG_DESCRIPTION= ? WHERE LOG_ID = ?", ('Teste de Banco', 1))
# print(response.message)