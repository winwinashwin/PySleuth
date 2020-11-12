import threading

from ...output import Loggers


class BaseComponent(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(BaseComponent, self).__init__(*args, **kwargs)

        self.logger = None
        self.daemon = True

    def initLogger(self, name: str, file: str) -> None:
        if not self.logger:
            self.logger = Loggers.getComponent(name, file)

    def log(self, *args):
        self.logger.info(*args)
