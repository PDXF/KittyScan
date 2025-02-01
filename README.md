
```markdown
# KittyScanApp

KittyScanApp is a user-friendly document scanning application built using `customtkinter`, Python's `subprocess`, and `Pillow` for image manipulation. It provides a simple interface to scan, display, export, and manage documents.

## Features

- **Scan Documents**: Scan documents using a connected scanner and save them in various formats (PNG, JPEG, PDF).
- **Display Image**: View the latest scan on the app’s main window.
- **Export Document**: Export the latest scan to a chosen location in the preferred format.
- **Settings**: Configure settings such as resolution, color mode, file format, and auto-save functionality.
- **Scan History**: View a history of previously scanned files.

## Requirements

- **Python 3.x**: Make sure Python 3 is installed on your system.
- **`customtkinter`**: For the custom GUI framework.
- **`Pillow`**: For image handling and display.
- **`scanimage`**: Command-line tool for document scanning (usually available on Linux but needs installation on macOS).
- **`tkinter`**: For creating the graphical user interface (usually comes pre-installed with Python).

### Install Dependencies

To install the necessary dependencies, run:

```bash
pip install customtkinter pillow
```

Additionally, if you're on macOS, you may need to install `scanimage` (part of the SANE project) to use your scanner. This might require additional setup as macOS doesn't provide a package manager like Linux. You can check out [SANE project](http://www.sane-project.org/) for more details or consider installing via [Homebrew](https://brew.sh/) if possible.

### Setting Up `kittyscan` Command on macOS

1. **Make the Python Script Executable**:

   Navigate to the directory where `KittyScan.py` is located and make the script executable by running the following command in your terminal:

   ```bash
   chmod +x KittyScan.py
   ```

2. **Create a Symlink for Easy Access**:

   Next, create a symbolic link (`symlink`) to a directory in your `$PATH`, such as `/usr/local/bin`, to make the command `kittyscan` available globally. Replace `/path/to/KittyScan/KittyScan.py` with the actual path to the `KittyScan.py` file.

   ```bash
   sudo ln -s /path/to/KittyScan/KittyScan.py /usr/local/bin/kittyscan
   ```

3. **Run the Application**:

   After the symlink is set up, you can run the app from any terminal window by simply typing:

   ```bash
   kittyscan
   ```

   This will launch the KittyScan application.

## Usage

1. **Start the Application**: After setting up the `kittyscan` command, simply type `kittyscan` in the terminal to start the app.

2. **Scanning**:
    - Click the **Scan** button to scan a document. The scan will be saved in the default file format and resolution.
    - View the scanned document on the main window.

3. **Exporting**:
    - Click the **Export** button to save the latest scanned document to your preferred location and format.

4. **Settings**:
    - Click the **Settings** button to configure various options such as resolution, color mode, and file format.
    - The Auto-save option will save scans automatically after each scan.

5. **History**:
    - Click the **History** button to view a list of all scanned files.

## Customization

The app offers the following configurable options:
- **Resolution**: Choose between 150, 300, or 600 DPI.
- **Color Mode**: Select between color or black & white scans.
- **File Format**: Choose from PNG, JPEG, or PDF.
- **Auto-save**: Enable or disable auto-saving after scanning.
- **Scan Area**: Configure whether you want to scan the full page or a custom region.

## Screenshots

Insert images here (if applicable)

## Contributing

If you would like to contribute to the development of `KittyScanApp`, feel free to open issues or submit pull requests. Contributions are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, contact valkdevices@gmail.com.
```

### Issue with `kittyscan` Command:

If the `kittyscan` command is not working after creating the symlink, you might want to check:

1. **Check if `/usr/local/bin` is in your `$PATH`**:
   Run `echo $PATH` to ensure `/usr/local/bin` is included. If it's not, add it by modifying your `.zshrc` or `.bash_profile` (depending on your shell).

   ```bash
   export PATH="/usr/local/bin:$PATH"
   ```

2. **Check Permissions**:
   Ensure that the symlink is correctly created and the file is executable. You can check if it's in place with `ls -l /usr/local/bin/kittyscan`.
