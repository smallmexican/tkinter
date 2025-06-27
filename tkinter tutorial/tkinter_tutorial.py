# Tkinter Tutorial - Step by Step Guide
# This tutorial will walk you through the basics of creating GUI applications with tkinter

import tkinter as tk
from tkinter import ttk, messagebox, filedialog

print("=== TKINTER TUTORIAL ===")
print("This tutorial covers the basics of tkinter GUI programming")
print("Each section builds upon the previous one")
print("\nLet's start with the basics!\n")

# ==========================================
# STEP 1: Creating Your First Window
# ==========================================

def step1_basic_window():
    """Step 1: Create a basic window"""
    print("STEP 1: Creating a basic window")
    
    # Create the main window (root)
    root = tk.Tk()
    
    # Set window title
    root.title("My First Tkinter Window")
    
    # Set window size (width x height)
    root.geometry("400x300")
    
    # Set window background color
    root.config(bg="lightblue")
    
    # Start the event loop (keeps window open)
    root.mainloop()

# ==========================================
# STEP 2: Adding Basic Widgets
# ==========================================

def step2_basic_widgets():
    """Step 2: Add labels, buttons, and basic widgets"""
    print("STEP 2: Adding basic widgets")
    
    root = tk.Tk()
    root.title("Basic Widgets")
    root.geometry("400x300")
    root.config(bg="white")
    
    # Label widget
    label = tk.Label(root, text="Hello, Tkinter!", 
                    font=("Arial", 16), 
                    fg="blue", 
                    bg="white")
    label.pack(pady=10)
    
    # Button widget
    def button_click():
        print("Button was clicked!")
        messagebox.showinfo("Info", "Button clicked!")
    
    button = tk.Button(root, text="Click Me!", 
                      command=button_click,
                      font=("Arial", 12),
                      bg="lightgreen",
                      fg="black")
    button.pack(pady=10)
    
    # Entry widget (text input)
    entry = tk.Entry(root, font=("Arial", 12), width=20)
    entry.pack(pady=10)
    entry.insert(0, "Type here...")
    
    root.mainloop()

# ==========================================
# STEP 3: Layout Management - Pack
# ==========================================

def step3_pack_layout():
    """Step 3: Understanding pack() layout manager"""
    print("STEP 3: Pack layout manager")
    
    root = tk.Tk()
    root.title("Pack Layout")
    root.geometry("400x300")
    
    # Pack with different sides
    tk.Label(root, text="Top", bg="red", fg="white").pack(side=tk.TOP, fill=tk.X)
    tk.Label(root, text="Bottom", bg="blue", fg="white").pack(side=tk.BOTTOM, fill=tk.X)
    tk.Label(root, text="Left", bg="green", fg="white").pack(side=tk.LEFT, fill=tk.Y)
    tk.Label(root, text="Right", bg="orange", fg="white").pack(side=tk.RIGHT, fill=tk.Y)
    tk.Label(root, text="Center", bg="purple", fg="white").pack(expand=True)
    
    root.mainloop()

# ==========================================
# STEP 4: Layout Management - Grid
# ==========================================

def step4_grid_layout():
    """Step 4: Understanding grid() layout manager"""
    print("STEP 4: Grid layout manager")
    
    root = tk.Tk()
    root.title("Grid Layout")
    root.geometry("400x300")
    
    # Create a calculator-like layout
    tk.Label(root, text="Calculator Layout", font=("Arial", 14)).grid(row=0, column=0, columnspan=3, pady=10)
    
    # Entry field
    entry = tk.Entry(root, font=("Arial", 12), width=20)
    entry.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
    
    # Buttons in grid
    buttons = [
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2),
        ('0', 5, 1), ('+', 5, 2)
    ]
    
    for (text, row, col) in buttons:
        tk.Button(root, text=text, width=5, height=2).grid(row=row, column=col, padx=2, pady=2)
    
    root.mainloop()

# ==========================================
# STEP 5: Interactive Application
# ==========================================

def step5_interactive_app():
    """Step 5: Create an interactive application"""
    print("STEP 5: Interactive application")
    
    root = tk.Tk()
    root.title("Interactive App - Name Greeter")
    root.geometry("400x300")
    root.config(bg="lightgray")
    
    # Variables to store data
    name_var = tk.StringVar()
    result_var = tk.StringVar()
    result_var.set("Enter your name and click greet!")
    
    # Title
    title_label = tk.Label(root, text="Name Greeter App", 
                          font=("Arial", 18, "bold"), 
                          bg="lightgray")
    title_label.pack(pady=20)
    
    # Name input frame
    input_frame = tk.Frame(root, bg="lightgray")
    input_frame.pack(pady=10)
    
    tk.Label(input_frame, text="Your Name:", font=("Arial", 12), bg="lightgray").pack(side=tk.LEFT)
    name_entry = tk.Entry(input_frame, textvariable=name_var, font=("Arial", 12), width=20)
    name_entry.pack(side=tk.LEFT, padx=5)
    
    # Functions for buttons
    def greet():
        name = name_var.get().strip()
        if name:
            result_var.set(f"Hello, {name}! Nice to meet you!")
        else:
            result_var.set("Please enter your name first!")
    
    def clear():
        name_var.set("")
        result_var.set("Enter your name and click greet!")
    
    # Buttons frame
    button_frame = tk.Frame(root, bg="lightgray")
    button_frame.pack(pady=10)
    
    greet_btn = tk.Button(button_frame, text="Greet Me!", 
                         command=greet, 
                         bg="lightgreen", 
                         font=("Arial", 12))
    greet_btn.pack(side=tk.LEFT, padx=5)
    
    clear_btn = tk.Button(button_frame, text="Clear", 
                         command=clear, 
                         bg="lightcoral", 
                         font=("Arial", 12))
    clear_btn.pack(side=tk.LEFT, padx=5)
    
    # Result display
    result_label = tk.Label(root, textvariable=result_var, 
                           font=("Arial", 12), 
                           bg="white", 
                           relief="sunken", 
                           wraplength=350)
    result_label.pack(pady=20, padx=20, fill=tk.X)
    
    # Bind Enter key to greet function
    root.bind('<Return>', lambda event: greet())
    
    root.mainloop()

# ==========================================
# STEP 6: Advanced Widgets
# ==========================================

def step6_advanced_widgets():
    """Step 6: Explore advanced widgets"""
    print("STEP 6: Advanced widgets")
    
    root = tk.Tk()
    root.title("Advanced Widgets")
    root.geometry("500x400")
    
    # Notebook (tabs)
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Tab 1: Checkboxes and Radio buttons
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text="Checkboxes & Radio")
    
    tk.Label(tab1, text="Choose your favorite colors:", font=("Arial", 12)).pack(pady=10)
    
    # Checkboxes
    colors = ["Red", "Green", "Blue", "Yellow"]
    color_vars = {}
    for color in colors:
        var = tk.BooleanVar()
        color_vars[color] = var
        tk.Checkbutton(tab1, text=color, variable=var, font=("Arial", 10)).pack(anchor=tk.W, padx=20)
    
    # Radio buttons
    tk.Label(tab1, text="Choose your favorite animal:", font=("Arial", 12)).pack(pady=(20, 10))
    animal_var = tk.StringVar()
    animals = ["Dog", "Cat", "Bird", "Fish"]
    for animal in animals:
        tk.Radiobutton(tab1, text=animal, variable=animal_var, value=animal, font=("Arial", 10)).pack(anchor=tk.W, padx=20)
    
    def show_selections():
        selected_colors = [color for color, var in color_vars.items() if var.get()]
        selected_animal = animal_var.get()
        messagebox.showinfo("Selections", 
                           f"Colors: {', '.join(selected_colors) if selected_colors else 'None'}\n"
                           f"Animal: {selected_animal if selected_animal else 'None'}")
    
    tk.Button(tab1, text="Show Selections", command=show_selections, bg="lightblue").pack(pady=20)
    
    # Tab 2: Listbox and Scrollbar
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text="Lists & Scrollbars")
    
    tk.Label(tab2, text="Programming Languages:", font=("Arial", 12)).pack(pady=10)
    
    # Frame for listbox and scrollbar
    list_frame = tk.Frame(tab2)
    list_frame.pack(pady=10)
    
    # Listbox with scrollbar
    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, width=30, height=10)
    languages = ["Python", "Java", "C++", "JavaScript", "C#", "Ruby", "Go", "Rust", "Swift", "Kotlin", "PHP", "R"]
    for lang in languages:
        listbox.insert(tk.END, lang)
    listbox.pack(side=tk.LEFT)
    
    scrollbar.config(command=listbox.yview)
    
    def show_selection():
        selection = listbox.curselection()
        if selection:
            selected_lang = listbox.get(selection[0])
            messagebox.showinfo("Selection", f"You selected: {selected_lang}")
    
    tk.Button(tab2, text="Show Selection", command=show_selection, bg="lightgreen").pack(pady=10)
    
    root.mainloop()

# ==========================================
# STEP 7: Complete Application Example
# ==========================================

def step7_complete_app():
    """Step 7: Complete application - Simple Text Editor"""
    print("STEP 7: Complete application - Simple Text Editor")
    
    root = tk.Tk()
    root.title("Simple Text Editor")
    root.geometry("600x400")
    
    # Variables
    current_file = None
    
    # Text widget with scrollbar
    text_frame = tk.Frame(root)
    text_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    text_widget = tk.Text(text_frame, wrap=tk.WORD, font=("Arial", 11))
    scrollbar = tk.Scrollbar(text_frame, command=text_widget.yview)
    text_widget.config(yscrollcommand=scrollbar.set)
    
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Functions
    def new_file():
        nonlocal current_file
        text_widget.delete(1.0, tk.END)
        current_file = None
        root.title("Simple Text Editor - New File")
    
    def open_file():
        nonlocal current_file
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                text_widget.delete(1.0, tk.END)
                text_widget.insert(1.0, content)
            current_file = file_path
            root.title(f"Simple Text Editor - {file_path}")
    
    def save_file():
        nonlocal current_file
        if current_file:
            with open(current_file, 'w') as file:
                file.write(text_widget.get(1.0, tk.END + "-1c"))
            messagebox.showinfo("Saved", f"File saved: {current_file}")
        else:
            save_as_file()
    
    def save_as_file():
        nonlocal current_file
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            with open(file_path, 'w') as file:
                file.write(text_widget.get(1.0, tk.END + "-1c"))
            current_file = file_path
            root.title(f"Simple Text Editor - {file_path}")
            messagebox.showinfo("Saved", f"File saved: {file_path}")
    
    # Menu bar
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
    file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
    file_menu.add_separator()
    file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
    file_menu.add_command(label="Save As", command=save_as_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    
    # Keyboard shortcuts
    root.bind('<Control-n>', lambda e: new_file())
    root.bind('<Control-o>', lambda e: open_file())
    root.bind('<Control-s>', lambda e: save_file())
    
    # Status bar
    status_bar = tk.Label(root, text="Ready", relief=tk.SUNKEN, anchor=tk.W)
    status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def update_status(event=None):
        cursor_pos = text_widget.index(tk.INSERT)
        line, col = cursor_pos.split('.')
        status_bar.config(text=f"Line: {line}, Column: {int(col)+1}")
    
    text_widget.bind('<KeyRelease>', update_status)
    text_widget.bind('<ButtonRelease>', update_status)
    
    root.mainloop()

# ==========================================
# TUTORIAL MENU
# ==========================================

def main_menu():
    """Main menu to select tutorial steps"""
    root = tk.Tk()
    root.title("Tkinter Tutorial Menu")
    root.geometry("400x500")
    root.config(bg="lightblue")
    
    tk.Label(root, text="Tkinter Tutorial", 
            font=("Arial", 20, "bold"), 
            bg="lightblue", 
            fg="darkblue").pack(pady=20)
    
    tk.Label(root, text="Choose a tutorial step:", 
            font=("Arial", 12), 
            bg="lightblue").pack(pady=10)
    
    steps = [
        ("Step 1: Basic Window", step1_basic_window),
        ("Step 2: Basic Widgets", step2_basic_widgets),
        ("Step 3: Pack Layout", step3_pack_layout),
        ("Step 4: Grid Layout", step4_grid_layout),
        ("Step 5: Interactive App", step5_interactive_app),
        ("Step 6: Advanced Widgets", step6_advanced_widgets),
        ("Step 7: Complete App", step7_complete_app),
    ]
    
    for step_name, step_function in steps:
        tk.Button(root, text=step_name, 
                 command=step_function,
                 font=("Arial", 11),
                 bg="white",
                 width=25,
                 pady=5).pack(pady=5)
    
    tk.Button(root, text="Exit Tutorial", 
             command=root.quit,
             font=("Arial", 11),
             bg="lightcoral",
             width=25,
             pady=5).pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main_menu()
