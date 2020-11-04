from dotenv import load_dotenv
from pathlib import Path

from pysleuth import PySleuth

envFile = Path(".") / ".env"
load_dotenv(envFile)


sleuth = PySleuth()
sleuth.start()

sleuth.mainLoop()
