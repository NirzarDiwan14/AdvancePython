class FileClassifier:
    """
    Determines file category based on extension.
    """

    DEFAULT_CATEGORY = "Others"

    EXTENSION_MAP = {
        "PDF" : [".pdf"],
        "Images" : [".jpg",".jpeg",".png",".gif",".bmp"],
        "Videos" : [".mp4",".avi",".mov",".mkv"],
        "Code": [".py", ".js", ".java", ".cpp", ".c", ".ts"],
        "Documents": [".docx", ".txt", ".xlsx", ".pptx"],
    }

    def classify(self,file_item):
        for category,extensions in self.EXTENSION_MAP.items():
            if file_item.extension in extensions:
                return category
        return self.DEFAULT_CATEGORY
    
