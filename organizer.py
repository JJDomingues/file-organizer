import os
import shutil
from datetime import datetime


class FileOrganizer:
    """Organize files by their last modification date.

    Files in ``folder_path`` that are not Python files (do not end with
    ``.py``) are moved into subfolders named ``YYYY-MM-DD`` based on their
    modification timestamps.
    """

    def __init__(self, folder_path: str):
        """Create a new :class:`FileOrganizer`.

        Args:
            folder_path: Directory whose contents will be organized.
        """
        self.folder_path = folder_path
        
    def __repr__(self) -> str:
        """Return a developer-friendly representation of the instance."""
        return f"FileOrganizer(folder='{self.folder_path}')"
    
    def list_files(self) -> list:
        """List all file and directory entries in ``folder_path``."""
        files = os.listdir(self.folder_path)
        return files
    
    def organizer_by_date(self) -> None:
        """Move files into date-based folders based on modification time."""

        files  = self.list_files()

        for file_name in files: 
            file_path = os.path.join(self.folder_path, file_name)

            if os.path.isfile(file_path) and not file_name.endswith(".py"):
                try: 
                    mod_time = os.path.getmtime(file_path)
                    date_str = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d")

                    dest_folder = os.path.join(self.folder_path, date_str)
                    os.makedirs(dest_folder, exist_ok=True)

                    shutil.move(file_path, os.path.join(dest_folder, file_name))
                    print(f"Moved: {file_name} -> {date_str}/")
                except PermissionError:
                    print(f"Skipped: {file_name} (no permisson)")
                except Exception as e:
                    print(f"Error moving {file_name}: {e}")
        
#tesntando 
organizer = FileOrganizer(".")
print (organizer)
print (organizer.list_files())
organizer.organizer_by_date()
