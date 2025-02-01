
import customtkinter as ctk
import subprocess
import os
import sys
from pathlib import Path
from PIL import Image, ImageTk
from tkinter import filedialog, Toplevel, Listbox, END, OptionMenu, StringVar, IntVar, Checkbutton

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
            result = subprocess.run(["scanimage", "--format", self.file_format.get(), "--resolution", self.resolution.get(), "--mode", self.color_mode.get(), "-o", output_path])
            
            if result.returncode == 0:
                self.scanned_files.append(output_path)
                self.update_image(output_path)
            else:
                print(f"Scan failed with error code {result.returncode}")
        except Exception as e:
            print(f"Error scanning document: {e}")
    
    def update_image(self, file_path):
        try:
            image = Image.open(file_path)
            image.thumbnail((500, 500))
            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo, text="")
            self.image_label.image = photo
        except Exception as e:
            print(f"Error updating image: {e}")

    def export_document(self):
        try:
            output_file = filedialog.asksaveasfilename(defaultextension=f".{self.file_format.get().lower()}", filetypes=[(f"{self.file_format.get()} files", f"*.{self.file_format.get().lower()}")])
            if output_file:
                # Simulate export action
                print(f"Document exported to {output_file}")
        except Exception as e:
            print(f"Error exporting document: {e}")

    def open_settings(self):
        settings_window = Toplevel(self)
        settings_window.title("Settings")
        settings_window.geometry("300x250")
        
        # Resolution setting
        resolution_label = ctk.CTkLabel(settings_window, text="Resolution:")
        resolution_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        resolution_menu = OptionMenu(settings_window, self.resolution, "150", "300", "600")
        resolution_menu.grid(row=0, column=1, padx=10, pady=10)

        # Color mode setting
        color_mode_label = ctk.CTkLabel(settings_window, text="Color Mode:")
        color_mode_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        color_mode_menu = OptionMenu(settings_window, self.color_mode, "Color", "Gray")
        color_mode_menu.grid(row=1, column=1, padx=10, pady=10)

        # File format setting
        file_format_label = ctk.CTkLabel(settings_window, text="File Format:")
        file_format_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        file_format_menu = OptionMenu(settings_window, self.file_format, "PNG", "JPEG", "TIFF")
        file_format_menu.grid(row=2, column=1, padx=10, pady=10)

        # Auto-save setting
        auto_save_check = Checkbutton(settings_window, text="Auto Save", variable=self.auto_save)
        auto_save_check.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Save button
        save_button = ctk.CTkButton(settings_window, text="Save", command=settings_window.destroy)
        save_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def open_history(self):
        history_window = Toplevel(self)
        history_window.title("Scan History")
        history_window.geometry("300x250")
        
        # History Listbox
        history_listbox = Listbox(history_window)
        history_listbox.pack(fill="both", expand=True)
        for file in self.scanned_files:
            history_listbox.insert(END, file)

        # Close button
        close_button = ctk.CTkButton(history_window, text="Close", command=history_window.destroy)
        close_button.pack(padx=10, pady=10)

if __name__ == "__main__":
    app = KittyScanApp()
    app.mainloop()
