# gui_repack_tgz
## To assemble a new exe is needed install Python and PyInstaller
### Download and install latest Python
* [python.org/downloads](https://www.python.org/downloads/windows/)
* [microsoft.com/store](https://apps.microsoft.com/store/search/python)
### Enter PowerShell and install pyinstaller module
```PowerShell
pip install pyinstaller
```
### Assemble a new exe
```PowerShell
python -m PyInstaller --onefile --noconsole main.py
```
### Run dist/main.exe