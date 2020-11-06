import telepot
from ...core.signal import Signal


class TelegramWrapper:
    SIG_msgReceived = Signal(str)

    def __init__(self, token: str, adminID: int):
        self.token = token
        self.adminID = adminID
        self.prevID = 669960286
        self._bot = telepot.Bot(token)
        try:
            resp = self._bot.getMe()
            assert resp["is_bot"]
        except AssertionError:
            # TODO: 
            pass
        except Exception as e:
            print(e)
            quit(1)    

    def spinOnce(self):
        updates = self._bot.getUpdates(self.prevID + 1)
        if not updates:
            return

        update = updates[0]
        self.prevID = update["update_id"]

        senderID = update["message"]["from"]["id"]

        if senderID != self.adminID:
            return

        msg = update["message"]["text"]
        if msg:
            self._onNewMessage(msg)            

    def _onNewMessage(self, msg):
        self.SIG_msgReceived.emit(msg)
    
    def sendText(self, text: str):
        self._bot.sendMessage(self.adminID, text)
    
    def sendDocument(self, filepath: str):
        with open(filepath, "rb") as fp:
            self._bot.sendDocument(self.adminID, fp)
