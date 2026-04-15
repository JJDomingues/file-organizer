import os


class FileOrganizer:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path
        
    def __repr__(self) -> str:
        return f"FileOrganizer(folder='{self.folder_path}')"
    
    def list_files(self) -> list:
        files = os.listdir(self.folder_path)
        return files
    
#tesntando 
organizer = FileOrganizer(".")
print (organizer)
print (organizer.list_files())
