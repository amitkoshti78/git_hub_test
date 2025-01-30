import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def on_click(event=None):
    file_path = filedialog.askopenfilename()
    try:
        with open(file_path, "r") as file_handle:
            file_lines = file_handle.readlines()
            my_text.delete(1.0, tk.END)
            for line in file_lines:
                my_text.insert(tk.END, line)

    except FileNotFoundError:
        messagebox.showerror("Error", "File not found")
    except Exception as err:
        messagebox.showerror("Error", str(err))

window = tk.Tk()
window.title("My Application")
window.geometry("400x400")

my_label = tk.Label(window, text="Welcome to my application")
my_label.pack(padx=10, pady=10)

name_entry = tk.Entry(window, width=30)
name_entry.pack(padx=10, pady=10)

my_text = tk.Text(window,height=5, width=50)
my_text.pack(padx=10, pady=10)

open_button = tk.Button(window, text="Open file", command=lambda : on_click())
open_button.pack(padx=10, pady=10)

close_button = tk.Button(window, text="Close", command=window.destroy)
close_button.pack(padx=10, pady=10)

window.mainloop()
