import logging
from app.config import config

def setup_logging():
    logging.basicConfig(
        level=config.log_level,
        format="%(levelname)s: %(message)s",
    )
