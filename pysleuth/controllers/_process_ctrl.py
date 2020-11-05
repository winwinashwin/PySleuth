from ..core.components import ProcessMonitor
from .base import BaseController
from ..configuration import ConfigHandler


class ProcessMntrController(BaseController):
    def __init__(self):
        super(ProcessMntrController, self).__init__()

        self.worker = ProcessMonitor()
        self.worker.initLogger("proc")

        cfg = ConfigHandler().getCfgComponent("PROCESS_MONITOR")
        self.worker.setPause(cfg.getint("log-every"))

        self.connectSlots()

    def startWorker(self):
        self.worker.start()

    def connectSlots(self):
        self.worker.SIG_process.connect(self, "onNewProcess")

    def onNewProcess(self, procName: str):
        self.worker.log(procName)
