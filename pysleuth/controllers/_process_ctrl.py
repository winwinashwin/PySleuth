from ..core.components import ProcessMonitor
from .base import BaseController


class ProcessController(BaseController):
    def __init__(self):
        super(ProcessController, self).__init__()

        self.worker = ProcessMonitor()
        self.worker.initLogger("proc")

        self.connectSlots()
    
    def startWorker(self):
        self.worker.start()

    def connectSlots(self):
        self.worker.SIG_process.connect(self, "onNewProcess")
    
    def onNewProcess(self, procName: str):
        self.worker.log(procName)