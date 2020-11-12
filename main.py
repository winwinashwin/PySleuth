from dotenv import load_dotenv
import os

from pysleuth.config import loadConfig


projectRoot = os.path.dirname(os.path.realpath(__file__))
envFile = os.path.join(projectRoot, ".env")
cfgFile = os.path.join(projectRoot, "settings.yml")

load_dotenv(envFile)
loadConfig(cfgFile)

if __name__ == "__main__":
    from pysleuth.app import PySleuth

    prog = PySleuth()
    prog.start()
