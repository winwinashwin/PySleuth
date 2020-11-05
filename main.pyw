from pysleuth.configuration import loadConfig
from dotenv import load_dotenv
from pathlib import Path

envFile = Path(".") / ".env"
cfgFile = Path(".") / "settings.cfg"


load_dotenv(envFile)
loadConfig(cfgFile)


if __name__ == "__main__":
    from pysleuth.prog import PySleuth

    prog = PySleuth()
    prog.start()

    prog.mainLoop()
