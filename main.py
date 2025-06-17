import logging
from utils.helper import greet
import yaml

logging.basicConfig(
    filename="/kaggle/working/log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

with open("config/config.yaml") as f:
    cfg = yaml.safe_load(f)

name = cfg.get("name", "World")
msg = greet(name)

logging.info(f"Greeting message: {msg}")

with open("/kaggle/working/output.txt", "w") as f:
    f.write(msg + "\n")
