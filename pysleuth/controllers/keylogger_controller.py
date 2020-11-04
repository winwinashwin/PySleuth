from ..components.keylogger import KeyLogger


class KeyLoggerController:
    def __init__(self):
        self.worker = KeyLogger()
        self.worker.KEY_PRESSED.connect(self, "onKeyPress")

    def startWorker(self):
        self.worker.start()

    def onKeyPress(self, key):
        # TODO
        pass
