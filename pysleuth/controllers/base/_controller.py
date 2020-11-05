import abc


class BaseController(metaclass=abc.ABCMeta):
    def __init__(self, master):
        self.master = master
        pass

    @abc.abstractmethod
    def startWorker(self):
        pass

    @abc.abstractmethod
    def connectSlots(self):
        pass
