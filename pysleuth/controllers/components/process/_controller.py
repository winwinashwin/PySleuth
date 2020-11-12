from ....core.components.process import ProcessMonitor
from ..._base import BaseController
from .... import config
from ....core import output


class ProcessMntrController(BaseController):
    def __init__(self):
        super(ProcessMntrController, self).__init__()

        self.worker = ProcessMonitor()
        logFile = output.Path().getRootDir() / "proc.log"
        self.worker.initLogger("proc.log", logFile)

        cfg = config.get().processMntr
        self.worker.setPause(cfg.logEvery)

        self.connectSlots()

    def startWorker(self):
        self.worker.start()

    def connectSlots(self):
        self.worker.SIG_process.connect(self, "onLogProcess")

    def onLogProcess(self, procName: str):
        self.worker.log(procName)
