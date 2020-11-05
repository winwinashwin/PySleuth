import threading

from ..loggers import Loggers


class BaseFeature(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(BaseFeature, self).__init__(*args, **kwargs)

        self.logger = None

    def run(self):
        pass

    def initLogger(self, name: str) -> None:
        if not self.logger:
            self.logger = Loggers.getNewLogger(name)
    
    def log(self, *args):
        self.logger.info(*args)