from pathlib import Path 
from organizer.classifier import FileClassifier
from organizer.organizer import Organizer
from organizer.app_logger import AppLogger

def main():
    target_directory = Path("sample_files")
    log_file = Path("logs/organizer.log")

    logger = AppLogger(log_file)
    classifier = FileClassifier()
    organizer = Organizer(
        target_dir = target_directory,
        classifier = classifier,
        logger = logger 
    )
    organizer.organize()
    print("File organization completed.")

if __name__ == "__main__":
    main()