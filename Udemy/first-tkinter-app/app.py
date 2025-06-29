import tkinter as tk
from tkinter import ttk

root = tk.Tk()

user_name = tk.StringVar()

name_label = ttk.Label(root, text="Name: ")
name_label.pack(side="left", padx=5, pady=5)
name_entry = ttk.Entry(root, textvariable=user_name, font=("Arial", 14), foreground="gray")
name_entry.pack(side="left", fill="x", expand=True, padx=5)
name_entry.focus()  # Set focus to the entry field



greet_button = ttk.Button(root, text="Greet", command=lambda: print(f"Hello, {user_name.get()}!"))
greet_button.pack(side="left")

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="right", padx=10)

root.mainloop()