# 📁 File Organizer

A Python script that automatically organizes files into folders by date.

## 🚀  Features 

- Lists all files in a directory
- Organizer files into subfolders by modification date (YYYY-MM-DD/`)
- Skips Python source files automatically
- Handles errors gracefully with try/except 

## 🛠️  Tech Stack 

- Python 3.9+
- `os` - file system navigation
- `shutil` - file moving
- `datetime` - date formatting

## 📦 How to Use

```python
from organizer import FileOrganizer

organizer = FileOrganizer("/path/to/your/folder")
organizer.organize_by_date()
```

## 👨‍💻 Author

**JJ Domingues** -  Self-taught develpoer building a career in Data & AI