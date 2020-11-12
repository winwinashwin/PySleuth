import abc


class BaseController(metaclass=abc.ABCMeta):
    def __init__(self):
        self.isWorkerActive = False

    @abc.abstractmethod
    def startWorker(self):
        pass

    @abc.abstractmethod
    def connectSlots(self):
        pass
