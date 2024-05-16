'''
# ****************************************************************************************
# Title: File Merger      	  |*******************************************************
# Developed by: ryanshatch   	  |*******************************************************
# Last Updated: May 15th 2024     |*******************************************************
# Version: 1.0                    |*******************************************************
# ****************************************************************************************
''''''************************************************************************************
#       Description: This script will combine csv files into one csv file.
# *************************************************************************************'''

import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
import json
import os

# Create window interface
root = tk.Tk()
root.title("File Merger")

file_path = []

# Browse your data to combine
def browse_files():
    global file_path
    file_path = filedialog.askopenfilenames(filetypes=[
        ("All Files", "*.*"),
        ("Text files", "*.txt"),
        ("SQL files", "*.sql"),
        ("CSV files", "*.csv"),
        ("CSVX files", "*.csvx"),
        ("Word documents", "*.docx"),
        ("XML files", "*.xml"),
        ("List files", "*.lst"),
        ("JSON files", "*.json")
    ])
    if file_path:
        tkinter.messagebox.showinfo("Files Selected", f"Selected {len(file_path)} files.")

# Function to read the content of different file types
def read_file(file_path):
    file_ext = os.path.splitext(file_path)[1].lower()
    content = ""
    encodings = ['utf-8-sig', 'utf-16', 'latin1', 'iso-8859-1']
    try:
        if file_ext in ['.txt', '.sql', '.csv', '.csvx', '.lst', '.xml']:
            for enc in encodings:
                try:
                    with open(file_path, 'r', encoding=enc) as file:
                        content = file.read()
                    break
                except UnicodeDecodeError:
                    continue
        elif file_ext == '.json':
            for enc in encodings:
                try:
                    with open(file_path, 'r', encoding=enc) as file:
                        data = json.load(file)
                        content = json.dumps(data, indent=4)
                    break
                except UnicodeDecodeError:
                    continue
        elif file_ext == '.docx':
            from docx import Document
            doc = Document(file_path)
            for para in doc.paragraphs:
                content += para.text + '\n'
    except Exception as e:
        tkinter.messagebox.showerror("Error", f"Failed to read {file_path}: {e}")
    return content

# Start combining
def merge_files():
    if not file_path:
        tkinter.messagebox.showerror("Error", "No files selected!")
        return
    if not file_name.get():
        tkinter.messagebox.showerror("Error", "Please enter a name for the combined file.")
        return
    
    combined_file_path = "{}.txt".format(file_name.get())  # Save as a .txt file to handle mixed content
    
    with open(combined_file_path, "w", encoding='utf-8-sig') as fout:
        for i, path in enumerate(file_path):
            content = read_file(path)
            if content:
                fout.write(content)
                fout.write("\n")  # Ensure each file's content is separated
    
    tkinter.messagebox.showinfo("Success", "Files successfully combined!")

# CREATE INTERFACE / GUI
file_name_text = tk.Label(root, text="New combined file name:", font=("Courier", 14))
file_name_text.grid(row=0, column=0, padx=10, pady=10)

file_name = tk.Entry(root, font=("Courier", 14))
file_name.grid(row=0, column=1, padx=10, pady=10)

skip_check = tk.IntVar()
skip_header = tk.Label(root, text="Skip header row:", font=("Courier", 14))
skip_header.grid(row=1, column=0, padx=10, pady=10)

radio_bu = tk.Checkbutton(root, variable=skip_check, font=("Courier", 14))
radio_bu.grid(row=1, column=1, padx=10, pady=10)

browse = tk.Button(root, command=browse_files, width=15, height=1, font=("Courier", 12), text="BROWSE")
browse.grid(row=2, column=0, padx=10, pady=10)

create = tk.Button(root, command=merge_files, foreground="red", width=10, height=1, font=("Courier", 12), text="CREATE")
create.grid(row=2, column=1, padx=10, pady=10)

# Mainloop TKINTER
root.mainloop()