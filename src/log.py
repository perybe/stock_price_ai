import logging
import os
from datetime import datetime


def configure_logging():
    if not os.path.exists("logs"):
        os.makedirs("logs")
    # Configure logging
    log_filename = f"logs/app.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler(log_filename), logging.StreamHandler()],
    )
