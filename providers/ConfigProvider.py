import configparser

from models.Config import ConfigSystem

class ConfigProvider():
    config = configparser.ConfigParser()
    __pathConfig = 'config.ini'

    def __init__(self) -> None:
        pass

    def getConfigSystem(self):
        self.config.read(self.__pathConfig)
        configData = self.config['SYSTEM']
        return ConfigSystem(
            DEBUG_MODE=configData['DEBUG_MODE']
        )


