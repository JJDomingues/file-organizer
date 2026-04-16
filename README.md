# 📁 File Organizer

A Python script that automatically organizes files into folders by date.

## 🚀 Features

- Lists all files in a directory
- Organizes files into subfolders by modification date (`YYYY-MM-DD/`)
- Skips Python source files automatically
- Handles errors gracefully with try/except

## ⚡ Tech Stack

- Python 3.9+
- `os` — file system navigation
- `shutil` — file moving
- `datetime` — date formatting

## 📦 Requirements

No external dependencies. Uses only Python standard library:
- `os`, `shutil`, `datetime`

## 🛠 How to Use

```python
from organizer import FileOrganizer

organizer = FileOrganizer("/path/to/your/folder")
organizer.organize_by_date()
```

## 👤 Author

**JJ Domingues** - Self-taught developer building a career in Data & AI
