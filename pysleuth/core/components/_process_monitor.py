import subprocess
import psutil
import time

from ..base import BaseComponent
from ..signal import Signal


class ProcessMonitor(BaseComponent):
    SIG_process = Signal(str)

    def __init__(self):
        super(ProcessMonitor, self).__init__()

        self.__pause = 5

    def run(self):
        while True:
            try:
                pid = subprocess.check_output(["xdotool", "getactivewindow", "getwindowpid"]).decode("utf-8").strip()

                p = psutil.Process(int(pid))
                self.SIG_process.emit(str(p.name()))
            except Exception as e:
                self.SIG_process.emit("Could not retrieve process info")
            
            time.sleep(self.pause)
    
    def setPause(self, pause: int):
        self.__pause = pause
    
    @property
    def pause(self):
        return self.__pause


