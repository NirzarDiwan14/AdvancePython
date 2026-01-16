from pathlib import Path

class FileItem: 
    """represents single file and its behaviours and encapsulates file-related data and behaviour."""

    def __init__(self,path : Path):
        if not path.is_file():
            raise ValueError(f"Provided path is not a file: {path}")
                             
        self.path = path
        self.name = path.name
        self.extension = path.suffix.lower()

    def move_to(self,  destination_dir : Path):
        """Move the file to a target directory.
        """
        destination_dir.mkdir(parents=True,exist_ok=True)
        destination = destination_dir / self.name
        self.path.rename(destination)
        self.path = destination