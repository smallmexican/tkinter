import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)  # Enable DPI awareness
except ImportError:
    pass

root = tk.Tk()

user_name = tk.StringVar()

details_frame = ttk.Frame(root, padding="10")
details_frame.pack(fill="x", expand=True)
name_label = ttk.Label(details_frame, text="Name: ")
name_label.pack(side="left", padx=5, pady=5)
name_entry = ttk.Entry(details_frame, textvariable=user_name, font=("Arial", 14), foreground="gray")
name_entry.pack(side="left", fill="x", expand=True, padx=5)
name_entry.focus()  # Set focus to the entry field

buttons_frame = ttk.Frame(root, padding="10")
buttons_frame.pack(fill="x", expand=True)

greet_button = ttk.Button(buttons_frame, text="Greet", command=lambda: print(f"Hello, {user_name.get()}!"))
greet_button.pack(side="left", fill="x", expand=True, padx=10)

quit_button = ttk.Button(buttons_frame, text="Quit", command=root.destroy)
quit_button.pack(side="left", fill="x", expand=True, padx=10)

root.mainloop()