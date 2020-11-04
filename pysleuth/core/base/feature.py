import threading


class BaseFeature(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(BaseFeature, self).__init__(*args, **kwargs)

    def run(self):
        pass
