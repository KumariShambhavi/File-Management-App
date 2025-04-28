import os
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

# Global Theme Settings
current_theme = "light"

light_theme = {
    "bg": "#e0f7fa",
    "fg": "#00796b",
    "button_bg": "#4caf50",
    "hover_bg": "#66bb6a"
}

dark_theme = {
    "bg": "#263238",
    "fg": "#eceff1",
    "button_bg": "#37474f",
    "hover_bg": "#455a64"
}

# Function to apply current theme
def apply_theme():
    colors = light_theme if current_theme == "light" else dark_theme
    root.config(bg=colors["bg"])
    title_label.config(bg=colors["bg"], fg=colors["fg"])
    for btn in buttons:
        btn.config(bg=colors["button_bg"], fg="white", activebackground=colors["hover_bg"], cursor="hand2")

# Function to toggle dark/light theme
def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    apply_theme()

# Function to create a file
def create_file():
    filename = simpledialog.askstring("Create File", "Enter filename:")
    if filename:
        try:
            path = filedialog.askdirectory(title="Choose Directory to Save File")
            if not path:
                return
            filepath = os.path.join(path, filename)
            with open(filepath, 'x') as f:
                messagebox.showinfo("Success", f"File '{filename}' created successfully!")
        except FileExistsError:
            messagebox.showwarning("Warning", f"File '{filename}' already exists!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Function to view all files in a selected folder
def view_all_files():
    path = filedialog.askdirectory(title="Select Directory to View Files")
    if not path:
        return
    files = os.listdir(path)
    if not files:
        messagebox.showinfo("Files", "No files found in the selected directory.")
    else:
        file_list = "\n".join(files)
        messagebox.showinfo("Files", f"Files in {path}:\n\n{file_list}")

# Function to delete a file
def delete_file():
    filepath = filedialog.askopenfilename(title="Select File to Delete")
    if filepath:
        try:
            os.remove(filepath)
            messagebox.showinfo("Deleted", f"File '{os.path.basename(filepath)}' deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Function to read a file
def read_file():
    filepath = filedialog.askopenfilename(title="Select File to Read")
    if filepath:
        try:
            with open(filepath, 'r') as f:
                content = f.read()
                top = tk.Toplevel(root)
                top.title(f"Reading {os.path.basename(filepath)}")
                text_area = tk.Text(top, wrap='word', font=("Helvetica", 12))
                text_area.insert('1.0', content)
                text_area.pack(expand=True, fill='both')
                top.geometry("600x400")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Function to write to a file
def write_file():
    filepath = filedialog.askopenfilename(title="Select File to Write")
    if filepath:
        try:
            content = simpledialog.askstring("Write", "Enter content to write:")
            if content is not None:
                with open(filepath, 'w') as f:
                    f.write(content)
                messagebox.showinfo("Success", f"Content written to '{os.path.basename(filepath)}' successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Function to append to a file
def append_file():
    filepath = filedialog.askopenfilename(title="Select File to Append")
    if filepath:
        try:
            content = simpledialog.askstring("Append", "Enter content to append:")
            if content is not None:
                with open(filepath, 'a') as f:
                    f.write('\n' + content)
                messagebox.showinfo("Success", f"Content appended to '{os.path.basename(filepath)}' successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Hover Effects
def on_enter(e):
    e.widget['bg'] = light_theme["hover_bg"] if current_theme == "light" else dark_theme["hover_bg"]

def on_leave(e):
    e.widget['bg'] = light_theme["button_bg"] if current_theme == "light" else dark_theme["button_bg"]

# Main GUI setup
root = tk.Tk()
root.title("📂 Professional File Manager")
root.geometry("500x650")
root.resizable(False, False)

# Set custom app icon (optional)
try:
    root.iconbitmap('myicon.ico')
except:
    pass

title_label = tk.Label(root, text="Professional File Manager", font=("Helvetica", 20, "bold"))
title_label.pack(pady=20)

btn_style = {"font": ("Helvetica", 14), "width": 30, "height": 2, "bd": 0}

# All buttons
buttons = []

btn_create = tk.Button(root, text="📄 Create File", command=create_file, **btn_style)
buttons.append(btn_create)
btn_create.pack(pady=8)

btn_view = tk.Button(root, text="📂 View All Files", command=view_all_files, **btn_style)
buttons.append(btn_view)
btn_view.pack(pady=8)

btn_delete = tk.Button(root, text="❌ Delete File", command=delete_file, **btn_style)
buttons.append(btn_delete)
btn_delete.pack(pady=8)

btn_read = tk.Button(root, text="📖 Read File", command=read_file, **btn_style)
buttons.append(btn_read)
btn_read.pack(pady=8)

btn_write = tk.Button(root, text="📝 Write to File", command=write_file, **btn_style)
buttons.append(btn_write)
btn_write.pack(pady=8)

btn_append = tk.Button(root, text="➕ Append to File", command=append_file, **btn_style)
buttons.append(btn_append)
btn_append.pack(pady=8)

btn_theme = tk.Button(root, text="🌓 Toggle Dark/Light Mode", command=toggle_theme, **btn_style)
buttons.append(btn_theme)
btn_theme.pack(pady=20)

btn_exit = tk.Button(root, text="🚪 Exit", command=root.destroy, **btn_style)
buttons.append(btn_exit)
btn_exit.pack(pady=20)

# Add hover effect to all buttons
for btn in buttons:
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Apply initial theme
apply_theme()

# Run the GUI
root.mainloop()
