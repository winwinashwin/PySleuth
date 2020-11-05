from PIL import ImageGrab
import time

from .base import BaseComponent
from ..signal import Signal


def saveScreenShot(filePath: str):
    ImageGrab.grab().save(filePath)


class ScreenMonitor(BaseComponent):
    SIG_grab = Signal()

    def __init__(self):
        super(ScreenMonitor, self).__init__()

        self.__pause = 5

    def run(self):
        while True:
            self.SIG_grab.emit()
            time.sleep(self.pause)

    def setPause(self, pause: int):
        self.__pause = pause

    @property
    def pause(self):
        return self.__pause
