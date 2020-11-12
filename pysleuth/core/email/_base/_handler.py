import abc


class BaseEmailHandler(metaclass=abc.ABCMeta):
    def __init__(self, progEmail: str, adminMail: str, pwd: str):
        self.progEmail = progEmail
        self.adminMail = adminMail
        self.pwd = pwd

    @abc.abstractmethod
    def login(self):
        pass

    @abc.abstractmethod
    def logout(self):
        pass
