from dotenv import load_dotenv
import os

from pysleuth.config import loadConfig, get
# from pysleuth.app import PySleuth

projectRoot = os.path.dirname(os.path.realpath(__file__))
envFile = os.path.join(projectRoot, ".env")
cfgFile = os.path.join(projectRoot, "settings.yml")

load_dotenv(envFile)
loadConfig(cfgFile)

# prog = PySleuth()
# prog.start()
# print(dir(get()))