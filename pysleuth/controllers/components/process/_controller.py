from ....core.components.process import ProcessMonitor
from ..._base import BaseController
from .... import config
from ....core import output

logger = output.Loggers.getMaster(__name__)


class ProcessMntrController(BaseController):
    def __init__(self):
        super(ProcessMntrController, self).__init__()

        self.worker = ProcessMonitor()
        logFile = output.Path().getRootDir() / "proc.log"
        self.worker.initLogger("proc.log", logFile)

        cfg = config.get().processMntr
        self.setWorkerPause(cfg.logEvery)

        self.worker.setPause(cfg.logEvery)

        self.connectSlots()

    def startWorker(self):
        self.worker.start()
        logger.info("Process monitoring active")

    def connectSlots(self):
        self.worker.SIG_process.connect(self, "onLogProcess")

    def onLogProcess(self, procName: str):
        self.worker.log(procName)
        logger.debug("Process monitor triggered")

    def setWorkerPause(self, pause: int):
        try:
            assert isinstance(pause, int) and pause > 0 and pause != None
        except AssertionError:
            logger.warn(
                f"Expected unsigned int, got: {pause}, setting to 5 second", exc_info=True)
            pause = 5

        self.worker.setPause(pause)
