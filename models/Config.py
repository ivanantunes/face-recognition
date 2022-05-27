class ConfigSystem():
    def __init__(self, DEBUG_MODE=bool, DEV_MODE=bool) -> None:
        self.DEBUG_MODE = DEBUG_MODE
        self.DEV_MODE = DEV_MODE

class ConfigLogin():
    def __init__(self, USERNAME=str, PASSWORD=str) -> None:
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD