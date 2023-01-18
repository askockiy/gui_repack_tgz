# gui_repack_tgz
This app is a simple graphical user interface that allows you to unpack a .tar.gz archive, make some changes to the contents, and then repack it into a new .tar.gz archive.
# Requirements
* Python 3.x
* Pyinstaller
# Installation
1. Download and install the latest version of Python from [python.org](https://www.python.org/downloads/windows/) or [microsoft.com](https://apps.microsoft.com/store/search/python)
2. Open PowerShell and install the pyinstaller module by running the command 
```PowerShell
pip install pyinstaller
```
3. Clone this repository and navigate to the root directory in PowerShell
4. Assemble the exe by running the command
```PowerShell
python -m PyInstaller --onefile --noconsole main.py
```
5. Run __dist/main.exe__

# Usage
1. Click the "Open" button and select the .tar.gz archive you wish to unpack
2. The contents of the archive will be extracted to a temporary directory
3. Make any desired changes to the contents of the temporary directory
4. Click the "Save as" button and select a location and name for the new archive
5. The temporary directory will be repacked into the new archive with the chosen name. The new archive will be saved in the location specified with the file extension .tar.gz
6. Click the "Exit" button to close the application.
# Note
* The temporary directory is deleted when the application is closed.
* The unpack and repack process is done using the __shutil__ module.
* The temporary directory is created using the __tempfile__ module.
* The GUI is created using the __tkinter__ module.