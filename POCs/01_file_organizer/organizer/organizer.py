from pathlib import Path 
from organizer.file_item import FileItem

class Organizer:
    """
    Orchestrates directory scanning, classification, and file movement.
    """

    def __init__(self,target_dir: Path ,classifier,logger):

        self.target_dir = target_dir
        self.classifier = classifier
        self.logger = logger

    def organize(self):
        if not self.target_dir.exists():
            raise FileNotFoundError(f"Directory not found: {self.target_dir}")
        
        for item in self.target_dir.iterdir():
            try:
                if item.is_file():
                    file_item = FileItem(item)
                    category = self.classifier.classify(file_item)
                    destination = self.target_dir / category
                    file_item.move_to(destination)
                    self.logger.info(
                        f"Moved '{file_item.name}' to '{category}'"
                    )

            except Exception as e:
                self.logger.error(f"Failed to process '{item}' : {e}")
        