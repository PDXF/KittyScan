#!/usr/bin/env python3

import customtkinter as ctk
import subprocess
import importlib
import os
import sys
from pathlib import Path
from PIL import Image, ImageTk
from tkinter import filedialog, Toplevel, Listbox, END, OptionMenu, StringVar, IntVar, Checkbutton

# Function to ensure the required libraries are installed
def install_library(library):
    try:
        importlib.import_module(library)  # Try importing the library
    except ImportError:
        try:
            # If the library is not installed, attempt to install it with pip or pip3
            subprocess.check_call([subprocess.sys.executable, "-m", "pip", "install", library])  # Try using pip
        except subprocess.CalledProcessError:
            subprocess.check_call([subprocess.sys.executable, "-m", "pip3", "install", library])  # Try using pip3

# Ensure required libraries are installed
install_library("customtkinter")
install_library("Pillow")

# Function to make the script executable
def make_executable():
    script_path = Path(__file__).resolve()
    command_name = "kittyscan"
    bin_dir = Path("/usr/local/bin")  # Standard directory for user binaries

    if not bin_dir.exists():
        print(f"Error: {bin_dir} does not exist.")
        return

    link_path = bin_dir / command_name

    # If a file or symlink already exists, remove it first
    if link_path.exists():
        try:
            os.remove(link_path)  # Remove the old file or symlink
            print(f"Removed old symlink or file: {link_path}")
        except Exception as e:
            print(f"Error removing old symlink or file: {e}")

    # Create the new symlink
    try:
        os.symlink(script_path, link_path)
        print(f"Successfully created the command '{command_name}'")
    except Exception as e:
        print(f"Error creating symlink: {e}")

# Check if this is the first run and make it executable if needed
if len(sys.argv) == 1 and not Path("/usr/local/bin/kittyscan").exists():
    make_executable()

# KittyScanApp class remains the same
class KittyScanApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("KittyScan")
        self.geometry("900x700")
        self.resizable(True, True)
        self.configure(bg="#1E1E2E")
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        
        self.scanned_files = []  # Store scanned history
        self.auto_save = IntVar(value=0)  # Auto-save setting
        self.resolution = StringVar(value="300")  # Resolution setting
        self.color_mode = StringVar(value="Color")  # Color mode setting
        self.file_format = StringVar(value="PNG")  # File format setting

        # Buttons frame
        self.button_frame = ctk.CTkFrame(self, fg_color="#2A2A3A")
        self.button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        # Scan button
        self.scan_button = ctk.CTkButton(self.button_frame, text="📷 Scan", command=self.scan_document, fg_color="#6D28D9")
        self.scan_button.pack(side="left", padx=5, pady=5)
        
        # Export button
        self.export_button = ctk.CTkButton(self.button_frame, text="💾 Export", command=self.export_document, fg_color="#9333EA")
        self.export_button.pack(side="left", padx=5, pady=5)
        
        # Settings button
        self.settings_button = ctk.CTkButton(self.button_frame, text="⚙️ Settings", command=self.open_settings, fg_color="#7C3AED")
        self.settings_button.pack(side="left", padx=5, pady=5)
        
        # History button
        self.history_button = ctk.CTkButton(self.button_frame, text="🕘 History", command=self.open_history, fg_color="#8B5CF6")
        self.history_button.pack(side="left", padx=5, pady=5)
        
        # Image display
        self.image_label = ctk.CTkLabel(self, text="No Scan Yet", bg_color="#1E1E2E", text_color="white")
        self.image_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
    def scan_document(self):
        try:
            output_path = f"scanned_{len(self.scanned_files) + 1}.{self.file_format.get().lower()}"
            result = subprocess.run(["scanimage", "--format", self.file_format.get().lower(), "--resolution", self.resolution.get()], capture_output=True)
            if result.returncode == 0:
                with open(output_path, "wb") as f:
                    f.write(result.stdout)
                self.scanned_files.append(output_path)
                self.display_image(output_path)
                if self.auto_save.get() == 1:
                    print(f"Auto-saved scan: {output_path}")
                print("Scan saved!")
            else:
                print("Error scanning: Scanner might be out of documents or disconnected.")
        except Exception as e:
            print(f"Error scanning: {e}")
    
    def display_image(self, path):
        try:
            img = Image.open(path)
            img.thumbnail((self.winfo_width() - 40, self.winfo_height() - 100))  # Keep aspect ratio
            img_ctk = ctk.CTkImage(light_image=img, size=img.size)
            
            self.image_label.configure(image=img_ctk, text="")
            self.image_label.image = img_ctk  # Keep reference
        except Exception as e:
            print(f"Error displaying image: {e}")
    
    def export_document(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=f".{self.file_format.get().lower()}", filetypes=[(f"{self.file_format.get()} Files", f"*.{self.file_format.get().lower()}")])
            if file_path:
                img = Image.open(self.scanned_files[-1])  # Export latest scan
                img.save(file_path, self.file_format.get())
                print(f"Exported as {self.file_format.get()}: {file_path}")
        except Exception as e:
            print(f"Error exporting: {e}")
    
    def open_settings(self):
        settings_window = Toplevel(self)
        settings_window.title("Settings")
        settings_window.geometry("500x500")
        settings_window.configure(bg="#2A2A3A")
        
        # Auto-save setting
        Checkbutton(settings_window, text="Auto-save Scans", variable=self.auto_save, bg="#2A2A3A", fg="white").pack(pady=10)
        
        # Resolution setting
        ctk.CTkLabel(settings_window, text="Select Resolution", text_color="white", bg_color="#2A2A3A").pack(pady=5)
        OptionMenu(settings_window, self.resolution, "150", "300", "600").pack(pady=10)
        
        # Color mode setting
        ctk.CTkLabel(settings_window, text="Select Color Mode", text_color="white", bg_color="#2A2A3A").pack(pady=5)
        OptionMenu(settings_window, self.color_mode, "Color", "Black & White").pack(pady=10)
        
        # File format setting
        ctk.CTkLabel(settings_window, text="Select File Format", text_color="white", bg_color="#2A2A3A").pack(pady=5)
        OptionMenu(settings_window, self.file_format, "PNG", "JPEG", "PDF").pack(pady=10)
        
        # Scan area setting (Optional, for advanced users)
        ctk.CTkLabel(settings_window, text="Scan Area", text_color="white", bg_color="#2A2A3A").pack(pady=5)
        OptionMenu(settings_window, StringVar(value="Full Page"), "Full Page", "Custom Region").pack(pady=10)
        
        # Dark Mode setting
        Checkbutton(settings_window, text="Dark Mode", variable=self.auto_save, bg="#2A2A3A", fg="white").pack(pady=10)
        
        # Reset button
        ctk.CTkButton(settings_window, text="Reset Settings", command=self.reset_settings, fg_color="#F43F5E").pack(pady=20)

    def reset_settings(self):
        self.auto_save.set(0)
        self.resolution.set("300")
        self.color_mode.set("Color")
        self.file_format.set("PNG")
        print("Settings have been reset to default.")
    
    def open_history(self):
        history_window = Toplevel(self)
        history_window.title("Scan History")
        history_window.geometry("400x300")
        history_window.configure(bg="#2A2A3A")
        
        listbox = Listbox(history_window, bg="#3B3B4F", fg="white")
        listbox.pack(fill="both", expand=True)
        
        for file in self.scanned_files:
            listbox.insert(END, file)

if __name__ == "__main__":
    app = KittyScanApp()
    app.mainloop()
