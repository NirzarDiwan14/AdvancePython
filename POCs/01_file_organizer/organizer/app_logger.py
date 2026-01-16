import logging 
from pathlib import Path

class AppLogger:
    """
    Centralized logging configuration.
    """

    def __init__(self,log_file: Path):
        log_file.parent.mkdir(parents=True,exist_ok=True)
        logging.basicConfig(
            filename = log_file,
            level = logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger = logging.getLogger("FileOrganizer")

    def info(self,message:str):
        self.logger.info(message)

    def error(self,message: str):
        self.logger.error(message)