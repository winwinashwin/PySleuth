from dotenv import load_dotenv
from pathlib import Path

from pysleuth import PySleuth, loadConfig

envFile = Path(".") / ".env"
cfgFile = Path(".") / "config.yml"

load_dotenv(envFile)
loadConfig(cfgFile)

prog = PySleuth()
prog.start()

prog.mainLoop()
