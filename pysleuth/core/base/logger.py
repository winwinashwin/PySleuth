import logging


class BaseLogger(object):
    def __init__(self):
        self.formatter = logging.Formatter('%(asctime)s: %(message)s')
    
    def new(self, name, file, level=logging.DEBUG):
        handler = logging.FileHandler(file)
        handler.setFormatter(self.formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)
        
        return logger
