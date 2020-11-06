from lib.config import loadConfig
from dotenv import load_dotenv
import os


projectRoot = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
envFile = os.path.join(projectRoot, ".env")
cfgFile = os.path.join(projectRoot, "settings.cfg")

load_dotenv(envFile)
loadConfig(cfgFile)

if __name__ == "__main__":
    from lib.app import PySleuth

    prog = PySleuth()
    prog.start()
