import logging
from utils.helper import greet
import yaml

logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)


fh = logging.FileHandler("/kaggle/working/log.txt")
fh.setLevel(logging.INFO)


formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)

with open("/kaggle/working/kaggle-module/config/config.yaml") as f:
    cfg = yaml.safe_load(f)

name = cfg.get("name", "World")
msg = greet(name)

logger.info(f"Greeting message: {msg}")


with open("/kaggle/working/output.txt", "w") as f:
    f.write(msg + "\n")
