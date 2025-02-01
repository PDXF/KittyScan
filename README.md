```markdown
# KittyScanApp

KittyScanApp is a simple document scanning app for macOS, built with Python. It lets you scan, view, and export documents with ease. 

## Features

- **Scan Documents**: Scan documents using a connected scanner.
- **View Scans**: See the scanned documents directly in the app.
- **Export**: Save your scanned documents as PNG, JPEG, or PDF.
- **Settings**: Adjust resolution, color mode, and file format.
- **Scan History**: View a history of your previous scans.

## Requirements

- **Python 3.x**: Make sure you have Python 3 installed. 
- **`customtkinter`**: For the GUI.
- **`Pillow`**: For handling images.
- **`scanimage`**: Command-line tool for scanning (needed on macOS too).
- **`tkinter`**: Pre-installed with Python.

## How to Install

### 1. Clone the Repo

First, open your terminal and clone the repository to your computer.

```bash
git clone https://github.com/your-username/KittyScan.git
```

This will create a folder named `KittyScan` on your computer.

### 2. Install Dependencies

Once you've cloned the repo, navigate to the project directory and install the necessary dependencies using `pip`:

```bash
cd KittyScan
pip install customtkinter pillow
```

If you're on macOS, you might also need to install `scanimage` for scanning. Please check the [SANE project](http://www.sane-project.org/) for installation instructions.

### 3. Make the Script Executable

Now, you need to make the script executable. Run this command:

```bash
chmod +x KittyScan.py
```

### 4. Create a Shortcut Command (`kittyscan`)

To make it easier to run the app, we'll create a shortcut command called `kittyscan`.

Find the full path to the `KittyScan.py` file on your computer. You can do this by typing `pwd` while in the `KittyScan` folder:

```bash
pwd
```

This will give you something like:

```
/Users/PDXF/KittyScan
```

Now, create a shortcut to `KittyScan.py` by running:

```bash
sudo ln -s /Users/PDXF/KittyScan/KittyScan.py /usr/local/bin/kittyscan
```

Make sure to replace `/Users/PDXF/KittyScan/KittyScan.py` with the correct path if it's different.

### 5. Run the App

After creating the shortcut, you can run the app by simply typing `kittyscan` in the terminal:

```bash
kittyscan
```

This will open the KittyScan app, and you're ready to start scanning!

## How to Use

1. **Start the Application**: Just type `kittyscan` in your terminal to launch the app.

2. **Scan a Document**: Click the **Scan** button to scan a document with your connected scanner.

3. **View the Scan**: The scanned document will show up in the app.

4. **Export the Scan**: To save the scan, click the **Export** button and choose where you want to save the document.

5. **Adjust Settings**: You can change scan settings like resolution, color mode, and file format in the **Settings** menu.

6. **View Scan History**: Check out your previous scans in the **History** tab.

## Customization

You can adjust the following options:

- **Resolution**: Choose from 150, 300, or 600 DPI.
- **Color Mode**: Select Color or Black & White.
- **File Format**: Choose PNG, JPEG, or PDF.
- **Auto-save**: Enable or disable auto-save after scanning.
- **Scan Area**: Full page or custom region.

## Contact

For questions or support, feel free to reach out to [Your Email].

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Summary of Key Steps:
1. **Clone the repo**: 
   ```bash
   git clone https://github.com/PDXF/KittyScan.git
   ```

2. **Install dependencies**: 
   ```bash
   cd KittyScan
   pip3 install customtkinter pillow
   ```

3. **Make the script executable**: 
   ```bash
   chmod +x KittyScan.py
   ```

4. **Create a symlink (shortcut)**: 
   Find the path to `KittyScan.py` with `pwd` and then create a shortcut:
   ```bash
   sudo ln -s /path/to/KittyScan/KittyScan.py /usr/local/bin/kittyscan
   ```

5. **Run the app**: 
   ```bash
   kittyscan
   ```

