
# How to create Python Program file to EXE

To convert a Python script into an executable file (.exe) using PyInstaller, follow these steps:



## 1. Install PyInstaller (if not already installed)
If you haven't installed pyinstaller, you can do so using pip:


```bash
  pip install pyinstaller
```


## 2. Navigate to your Python script's directory
Open the command prompt or terminal, and navigate to the directory where your Python script is located. Use the cd command:
    
  ```bash
    cd path\to\your\python\file
  ```

## 3. Use PyInstaller to Create the Executable
Run the following command in the terminal:

```bash
    pyinstaller --onefile --windowed your_script.py
```

## Explanation:
--onefile: This flag bundles everything into a single .exe file.

--windowed: This flag prevents a command prompt window from appearing when running the .exe. Use this flag for  GUI-based applications (like Tkinter).

your_script.py: Replace this with the name of your Python script.

## 4. Check the dist folder
After running the command, PyInstaller will create several directories and files:

A build folder (used by PyInstaller for temporary files).
A dist folder (this is where your .exe file will be created).
Navigate to the dist folder:

```bash
    cd dist
```

Inside, you'll find the .exe file with the same name as your Python script (e.g., your_script.exe).

## 5. Run your .exe file
Now, you can run the .exe file directly on a Windows machine without needing Python installed.

## Optional: Customizing the Build
You can customize how the .exe is built by adding more options to the pyinstaller command. Some useful options include:

--icon=icon.ico: To add an icon to the .exe file.
--add-data="path\to\data;.": To include extra files like images or databases.
For example:

```bash
pyinstaller --onefile --windowed --icon=myicon.ico --add-data="data\image.png;." your_script.py
```



## Authors

- [@tayade-aniket](https://github.com/tayade-aniket)

