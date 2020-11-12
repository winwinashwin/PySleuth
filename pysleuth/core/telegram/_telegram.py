import telepot
from ...core.signal import Signal


class TelegramWrapper:
    SIG_msgReceived = Signal(str)

    def __init__(self, token: str, adminID: int):
        self.token = token
        self.adminID = adminID
        self.prevID = 0
        self._bot = telepot.Bot(token)
        resp = self._bot.getMe()
        assert resp["is_bot"]

    def spinOnce(self):
        updates = self._bot.getUpdates(self.prevID + 1)
        if not updates:
            return

        update = updates[0]
        if self.prevID == 0:
            self.prevID = update["update_id"]
            return

        self.prevID = update["update_id"]

        senderID = update["message"]["from"]["id"]

        if senderID != self.adminID:
            return

        msg = update["message"]["text"]
        if msg:
            self._onNewMessage(msg)

    def _onNewMessage(self, msg):
        self.SIG_msgReceived.emit(msg)

    def sendText(self, text: str, **kwargs):
        self._bot.sendMessage(self.adminID, text, **kwargs)

    def sendDocument(self, filepath: str):
        with open(filepath, "rb") as fp:
            self._bot.sendDocument(self.adminID, fp)

    def sendPhoto(self, filepath: str):
        with open(filepath, "rb") as fp:
            self._bot.sendPhoto(self.adminID, fp)
