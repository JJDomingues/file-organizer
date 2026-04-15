import os

class FileOrganizer:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path
        
    def __repr__(self) -> str:
        return f"FileOrganizer(folder='{self.folder_path}')"
    
    def list_files(self) -> list:
        files = os.listdir(self.folder_path)
        return files
    
    def organizer_by_date(self) -> None:
        import shutil
        from datetime import datetime

        files  = self.list_files()

        for file_name in files: 
            file_path = os.path.join(self.folder_path, file_name)

            if os.path.isfile(file_path) and not file_name.endswith(".py"):
                mod_time = os.path.getmtime(file_path)
                date_str = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d")

                dest_folder = os.path.join(self.folder_path, date_str)
                os.makedirs(dest_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(dest_folder, file_name))
                print(f"Moved: {file_name} -> {date_str}/")
    
#tesntando 
organizer = FileOrganizer(".")
print (organizer)
print (organizer.list_files())
organizer.organizer_by_date()
