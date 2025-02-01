
```markdown
# KittyScanApp

KittyScanApp is a simple and user-friendly document scanning application built with `customtkinter`, Python's `subprocess`, and `Pillow`. This app allows users to scan, display, export, and manage scanned documents directly from their macOS terminal.

## Features

- **Scan Documents**: Scan documents from a connected scanner and save them in various formats (PNG, JPEG, PDF).
- **Display Image**: View the scanned document in the app’s main window.
- **Export Document**: Export the latest scan to your chosen location in the preferred file format.
- **Settings**: Configure settings such as resolution, color mode, file format, and auto-save functionality.
- **Scan History**: View a history of previously scanned documents.

## Requirements

- **Python 3.x**: Ensure Python 3 is installed on your macOS system.
- **customtkinter**: For the custom GUI framework.
- **Pillow**: For image handling and display.
- **scanimage**: Required for scanning documents (usually available for Linux but can work with compatible macOS tools).
- **tkinter**: Typically comes pre-installed with Python.

### Install Dependencies

To install the necessary Python dependencies, run:

```bash
pip install customtkinter pillow
```

### Installing `scanimage` on macOS

While `scanimage` is typically available on Linux, macOS users can try alternative scanning tools. One option is [SANE (Scanner Access Now Easy)](http://www.sane-project.org/) or a third-party application like [VueScan](https://www.hamrick.com/).

To install VueScan, you can follow the steps on their website.

## Setting Up KittyScanApp

1. **Clone the Repository**: First, clone the repository from GitHub to your local machine.

    ```bash
    git clone https://github.com/PDXF/KittyScan.git
    cd KittyScan
    ```

2. **Make `kittyscan` a Command**:
   To run `KittyScanApp` from your terminal with the `kittyscan` command, you’ll need to make the Python file executable.

    - Open the terminal and navigate to the `KittyScan` directory.
    - Run the following command to make the Python file executable:

      ```bash
      chmod +x KittyScan.py
      ```

    - Next, create a symbolic link to make it accessible globally via the `kittyscan` command:

      ```bash
      sudo ln -s /path/to/KittyScan/KittyScan.py /usr/local/bin/kittyscan
      ```

    Replace `/path/to/KittyScan/KittyScan.py` with the actual path where the `KittyScan.py` file is located.

    This will allow you to run the app by simply typing `kittyscan` in your terminal.

3. **Run KittyScan**:
    - Now you can run the app by simply typing `kittyscan` in the terminal:

    ```bash
    kittyscan
    ```

    The application will launch, and you can start scanning documents.

## Usage

1. **Start the Application**: Open your terminal and type `kittyscan` to start the app.

2. **Scanning**:
    - Click the **Scan** button to scan a document. The scan will be saved in the default file format and resolution.
    - The scanned document will be displayed in the app’s main window.

3. **Exporting**:
    - Click the **Export** button to save the latest scan to a location of your choice in your preferred format (PNG, JPEG, or PDF).

4. **Settings**:
    - Click the **Settings** button to configure various options such as resolution, color mode, and file format.
    - The auto-save option will automatically save your scan after each scan.

5. **History**:
    - Click the **History** button to view a list of previously scanned files.

## Customization

You can customize the following settings within the app:
- **Resolution**: Choose between 150, 300, or 600 DPI.
- **Color Mode**: Select either "Color" or "Black & White" scans.
- **File Format**: Choose from PNG, JPEG, or PDF.
- **Auto-save**: Enable or disable automatic saving of scans.
- **Scan Area**: Choose to scan the "Full Page" or a "Custom Region" (advanced users).
- **Dark Mode**: Toggle dark mode for a more comfortable viewing experience.

## Screenshots

Insert images here (if applicable)

## Contributing

Feel free to contribute by opening issues or submitting pull requests. Contributions are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Key Changes:
1. **Installation Instructions**: Added steps to clone the GitHub repo, make `KittyScan.py` executable, and link it to a command `kittyscan` globally.
2. **Run the App via Terminal**: The app can now be launched with `kittyscan` from the terminal after setting it up.
3. **macOS Focus**: Adjusted for macOS usage with VueScan or SANE as potential scanning solutions.

This should give users clear guidance on how to get the app up and running on their system. Let me know if you need any more tweaks!
