# TKINTER CHEAT SHEET - Complete Reference Guide

"""
====================================
TKINTER CHEAT SHEET - QUICK REFERENCE
====================================

This file contains all the essential tkinter functions, properties, and examples.
Use Ctrl+F to quickly find what you need!

TABLE OF CONTENTS:
1. Basic Setup
2. Main Widgets
3. Layout Managers
4. Widget Properties
5. Events and Bindings
6. Dialogs and Messages
7. Styling and Colors
8. Geometry and Positioning
9. Variables and Data Binding
10. Available Functions Reference
11. Common Patterns
12. Keyboard Shortcuts
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, font

# =====================================
# 1. BASIC SETUP
# =====================================

def basic_setup_example():
    # Create main window
    root = tk.Tk()
    root.title("Window Title")
    root.geometry("400x300")           # width x height
    root.geometry("400x300+100+50")   # width x height + x_offset + y_offset
    root.resizable(False, False)      # (width_resizable, height_resizable)
    root.config(bg="lightgray")       # Background color
    # root.iconbitmap("icon.ico")     # Window icon (optional - need actual icon file)
    
    # Start the event loop
    root.mainloop()

# =====================================
# 2. MAIN WIDGETS
# =====================================

def widgets_reference():
    root = tk.Tk()
    root.title("Widget Reference")
    root.geometry("600x800")
    
    # LABEL - Display text or images
    label = tk.Label(root, text="Hello World", font=("Arial", 12), 
                    fg="blue", bg="white")
    label.pack(pady=5)
    
    # BUTTON - Clickable button
    button = tk.Button(root, text="Click Me", command=lambda: print("Clicked!"),
                      bg="lightblue", fg="black", font=("Arial", 10))
    button.pack(pady=5)
    
    # ENTRY - Single line text input
    entry = tk.Entry(root, font=("Arial", 12), width=20)
    entry.pack(pady=5)
    entry.insert(0, "Default text")
    
    # TEXT - Multi-line text input
    text = tk.Text(root, width=40, height=5, font=("Arial", 10))
    text.pack(pady=5)
    text.insert("1.0", "Multi-line text here")
    
    # FRAME - Container for other widgets
    frame = tk.Frame(root, bg="lightgray", relief="raised", bd=2)
    frame.pack(pady=5, padx=10, fill="x")
    
    # CHECKBUTTON - Checkbox
    check_var = tk.BooleanVar()
    checkbutton = tk.Checkbutton(frame, text="Check me", variable=check_var)
    checkbutton.pack(side="left")
    
    # RADIOBUTTON - Radio button (single selection)
    radio_var = tk.StringVar()
    radio1 = tk.Radiobutton(frame, text="Option 1", variable=radio_var, value="1")
    radio2 = tk.Radiobutton(frame, text="Option 2", variable=radio_var, value="2")
    radio1.pack(side="left")
    radio2.pack(side="left")
    
    # LISTBOX - List of selectable items
    listbox = tk.Listbox(root, height=4)
    for item in ["Item 1", "Item 2", "Item 3", "Item 4"]:
        listbox.insert(tk.END, item)
    listbox.pack(pady=5)
    
    # SCALE - Slider
    scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=200)
    scale.pack(pady=5)
    
    # SPINBOX - Number input with up/down arrows
    spinbox = tk.Spinbox(root, from_=0, to=10, width=10)
    spinbox.pack(pady=5)
    
    # CANVAS - Drawing area
    canvas = tk.Canvas(root, width=200, height=100, bg="white")
    canvas.pack(pady=5)
    canvas.create_rectangle(10, 10, 50, 50, fill="red")
    canvas.create_oval(60, 10, 100, 50, fill="blue")
    
    # SCROLLBAR - Scroll control
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side="right", fill="y")
    
    # MENU - Menu bar
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=lambda: print("New"))
    file_menu.add_command(label="Open", command=lambda: print("Open"))
    
    root.mainloop()

# =====================================
# 3. LAYOUT MANAGERS
# =====================================

# PACK - Simple layout
def pack_examples():
    """
    pack() options:
    - side: tk.TOP, tk.BOTTOM, tk.LEFT, tk.RIGHT
    - fill: tk.X, tk.Y, tk.BOTH
    - expand: True/False
    - padx, pady: external padding
    - ipadx, ipady: internal padding
    """
    root = tk.Tk()
    
    tk.Label(root, text="Top", bg="red").pack(side=tk.TOP, fill=tk.X)
    tk.Label(root, text="Bottom", bg="blue").pack(side=tk.BOTTOM, fill=tk.X)
    tk.Label(root, text="Left", bg="green").pack(side=tk.LEFT, fill=tk.Y)
    tk.Label(root, text="Right", bg="yellow").pack(side=tk.RIGHT, fill=tk.Y)
    tk.Label(root, text="Center", bg="purple").pack(expand=True)
    
    root.mainloop()

# GRID - Table layout
def grid_examples():
    """
    grid() options:
    - row, column: position in grid
    - rowspan, columnspan: span multiple cells
    - sticky: tk.N, tk.S, tk.E, tk.W (or combinations like "nsew")
    - padx, pady: padding
    - ipadx, ipady: internal padding
    """
    root = tk.Tk()
    
    tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    tk.Entry(root).grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(root, text="Email:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    tk.Entry(root).grid(row=1, column=1, padx=5, pady=5)
    
    tk.Button(root, text="Submit").grid(row=2, column=0, columnspan=2, pady=10)
    
    root.mainloop()

# PLACE - Absolute positioning
def place_examples():
    """
    place() options:
    - x, y: absolute position
    - relx, rely: relative position (0.0 to 1.0)
    - width, height: absolute size
    - relwidth, relheight: relative size
    - anchor: tk.N, tk.S, tk.E, tk.W, tk.CENTER, etc.
    """
    root = tk.Tk()
    root.geometry("400x300")
    
    tk.Label(root, text="Top Left", bg="red").place(x=10, y=10)
    tk.Label(root, text="Center", bg="green").place(relx=0.5, rely=0.5, anchor="center")
    tk.Label(root, text="Bottom Right", bg="blue").place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
    
    root.mainloop()

# =====================================
# 4. WIDGET PROPERTIES
# =====================================

WIDGET_PROPERTIES = """
COMMON WIDGET PROPERTIES:

Visual Properties:
- bg, background: Background color
- fg, foreground: Text color
- font: Font specification
- relief: "flat", "raised", "sunken", "ridge", "groove"
- bd, borderwidth: Border width
- width, height: Widget dimensions

Text Properties:
- text: Display text
- textvariable: Link to StringVar
- justify: "left", "center", "right"
- anchor: Text position within widget
- wraplength: Text wrapping width

State Properties:
- state: "normal", "disabled", "active"
- cursor: Mouse cursor when hovering

Layout Properties:
- padx, pady: External padding
- ipadx, ipady: Internal padding
- sticky: Grid alignment

Button-specific:
- command: Function to call when clicked
- activebackground: Color when pressed
- activeforeground: Text color when pressed

Entry/Text-specific:
- show: Character to show (e.g., "*" for passwords)
- validate: Input validation
- textvariable: Link to StringVar for automatic updates
"""

# =====================================
# 5. EVENTS AND BINDINGS
# =====================================

def events_examples():
    root = tk.Tk()
    
    # Mouse events
    def on_click(event):
        print(f"Clicked at {event.x}, {event.y}")
    
    def on_right_click(event):
        print("Right clicked!")
    
    # Keyboard events
    def on_key_press(event):
        print(f"Key pressed: {event.keysym}")
    
    # Widget events
    def on_enter(event):
        event.widget.config(bg="lightblue")
    
    def on_leave(event):
        event.widget.config(bg="white")
    
    label = tk.Label(root, text="Hover over me!", bg="white", padx=20, pady=20)
    label.pack(pady=20)
    
    # Bind events
    label.bind("<Button-1>", on_click)        # Left click
    label.bind("<Button-3>", on_right_click)  # Right click
    label.bind("<Enter>", on_enter)           # Mouse enter
    label.bind("<Leave>", on_leave)           # Mouse leave
    
    root.bind("<KeyPress>", on_key_press)     # Any key press
    root.focus_set()  # Allow window to receive key events
    
    """
    COMMON EVENT PATTERNS:
    
    Mouse Events:
    - <Button-1>: Left mouse button
    - <Button-2>: Middle mouse button
    - <Button-3>: Right mouse button
    - <Double-Button-1>: Double click
    - <Motion>: Mouse movement
    - <Enter>: Mouse enters widget
    - <Leave>: Mouse leaves widget
    
    Keyboard Events:
    - <KeyPress>: Any key pressed
    - <KeyRelease>: Any key released
    - <Return>: Enter key
    - <BackSpace>: Backspace key
    - <Delete>: Delete key
    - <Tab>: Tab key
    - <Control-c>: Ctrl+C
    - <Alt-F4>: Alt+F4
    
    Window Events:
    - <Configure>: Window resized
    - <Destroy>: Window closed
    - <FocusIn>: Widget gains focus
    - <FocusOut>: Widget loses focus
    """
    
    root.mainloop()

# =====================================
# 6. DIALOGS AND MESSAGES
# =====================================

def dialogs_examples():
    root = tk.Tk()
    
    def show_info():
        messagebox.showinfo("Info", "This is an information message")
    
    def show_warning():
        messagebox.showwarning("Warning", "This is a warning message")
    
    def show_error():
        messagebox.showerror("Error", "This is an error message")
    
    def ask_question():
        result = messagebox.askyesno("Question", "Do you want to continue?")
        print(f"User answered: {result}")
    
    def ask_ok_cancel():
        result = messagebox.askokcancel("Confirm", "Are you sure?")
        print(f"User chose: {result}")
    
    def open_file():
        filename = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            print(f"Selected file: {filename}")
    
    def save_file():
        filename = filedialog.asksaveasfilename(
            title="Save file as",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            print(f"Save to: {filename}")
    
    # Create buttons for each dialog type
    tk.Button(root, text="Show Info", command=show_info).pack(pady=5)
    tk.Button(root, text="Show Warning", command=show_warning).pack(pady=5)
    tk.Button(root, text="Show Error", command=show_error).pack(pady=5)
    tk.Button(root, text="Ask Yes/No", command=ask_question).pack(pady=5)
    tk.Button(root, text="Ask OK/Cancel", command=ask_ok_cancel).pack(pady=5)
    tk.Button(root, text="Open File", command=open_file).pack(pady=5)
    tk.Button(root, text="Save File", command=save_file).pack(pady=5)
    
    root.mainloop()

# =====================================
# 7. STYLING AND COLORS
# =====================================

COLORS_AND_STYLING = """
COLOR SPECIFICATIONS:
- Named colors: "red", "blue", "green", "white", "black", etc.
- Hex colors: "#FF0000" (red), "#00FF00" (green), "#0000FF" (blue)
- RGB colors: Use hex format

FONT SPECIFICATIONS:
- Tuple format: ("Arial", 12, "bold")
- String format: "Arial 12 bold"
- Font styles: "normal", "bold", "italic", "underline"
- Common fonts: "Arial", "Times", "Courier", "Helvetica"

RELIEF STYLES:
- "flat": No border (modern look)
- "raised": Appears raised
- "sunken": Appears pressed in
- "ridge": Ridge border
- "groove": Groove border

CURSORS:
- "arrow": Default cursor
- "hand2": Hand pointer
- "ibeam": Text cursor
- "wait": Wait/hourglass
- "crosshair": Crosshair
- "question_arrow": Question mark
"""

def styling_examples():
    root = tk.Tk()
    root.title("Styling Examples")
    
    # Different font styles
    tk.Label(root, text="Normal Text", font=("Arial", 12)).pack(pady=2)
    tk.Label(root, text="Bold Text", font=("Arial", 12, "bold")).pack(pady=2)
    tk.Label(root, text="Italic Text", font=("Arial", 12, "italic")).pack(pady=2)
    tk.Label(root, text="Underlined Text", font=("Arial", 12, "underline")).pack(pady=2)
    
    # Different colors
    tk.Label(root, text="Red Text", fg="red").pack(pady=2)
    tk.Label(root, text="Blue Background", bg="#0000FF", fg="white").pack(pady=2)
    tk.Label(root, text="Green Text", fg="#00AA00").pack(pady=2)
    
    # Different relief styles
    for relief_style in ["flat", "raised", "sunken", "ridge", "groove"]:
        tk.Label(root, text=f"Relief: {relief_style}", relief=relief_style, 
                bd=2, padx=10, pady=5).pack(pady=2)
    
    root.mainloop()

# =====================================
# 10. AVAILABLE FUNCTIONS REFERENCE
# =====================================

TKINTER_FUNCTIONS_REFERENCE = """
=====================================
COMPLETE TKINTER FUNCTIONS REFERENCE
=====================================

WINDOW/ROOT METHODS:
├── Configuration
│   ├── root.title(string) - Set window title
│   ├── root.geometry(string) - Set size/position "WIDTHxHEIGHT+X+Y"
│   ├── root.resizable(width, height) - Allow/disable resizing
│   ├── root.minsize(width, height) - Set minimum size
│   ├── root.maxsize(width, height) - Set maximum size
│   ├── root.config(**options) - Configure window properties
│   ├── root.configure(**options) - Same as config()
│   ├── root.iconbitmap(filename) - Set window icon
│   └── root.state() - Get/set window state ("normal", "iconic", "withdrawn")
│
├── Control
│   ├── root.mainloop() - Start the event loop
│   ├── root.quit() - Exit the event loop
│   ├── root.destroy() - Destroy window and exit
│   ├── root.withdraw() - Hide window
│   ├── root.deiconify() - Show window
│   ├── root.lift() - Bring window to front
│   └── root.lower() - Send window to back
│
└── Information
    ├── root.winfo_width() - Get current width
    ├── root.winfo_height() - Get current height
    ├── root.winfo_x() - Get x position
    ├── root.winfo_y() - Get y position
    ├── root.winfo_screenwidth() - Get screen width
    ├── root.winfo_screenheight() - Get screen height
    └── root.winfo_children() - Get child widgets

WIDGET CREATION FUNCTIONS:
├── Basic Widgets
│   ├── tk.Label(parent, **options) - Display text/image
│   ├── tk.Button(parent, **options) - Clickable button
│   ├── tk.Entry(parent, **options) - Single-line text input
│   ├── tk.Text(parent, **options) - Multi-line text input
│   ├── tk.Frame(parent, **options) - Container widget
│   ├── tk.Canvas(parent, **options) - Drawing area
│   └── tk.Toplevel(parent, **options) - New window
│
├── Input Widgets
│   ├── tk.Checkbutton(parent, **options) - Checkbox
│   ├── tk.Radiobutton(parent, **options) - Radio button
│   ├── tk.Scale(parent, **options) - Slider
│   ├── tk.Spinbox(parent, **options) - Number input with arrows
│   ├── tk.Listbox(parent, **options) - List selection
│   └── tk.OptionMenu(parent, variable, *values) - Dropdown menu
│
├── Layout Widgets
│   ├── tk.Frame(parent, **options) - Basic container
│   ├── tk.LabelFrame(parent, **options) - Frame with title
│   ├── tk.PanedWindow(parent, **options) - Resizable panes
│   └── tk.Scrollbar(parent, **options) - Scroll control
│
└── Menu System
    ├── tk.Menu(parent, **options) - Menu container
    ├── tk.Menubutton(parent, **options) - Menu button
    └── menu.add_command() - Add menu item

WIDGET METHODS (Available on all widgets):
├── Layout Management
│   ├── widget.pack(**options) - Pack layout manager
│   ├── widget.grid(**options) - Grid layout manager
│   ├── widget.place(**options) - Place layout manager
│   ├── widget.pack_forget() - Remove from pack layout
│   ├── widget.grid_forget() - Remove from grid layout
│   └── widget.place_forget() - Remove from place layout
│
├── Configuration
│   ├── widget.config(**options) - Change widget properties
│   ├── widget.configure(**options) - Same as config()
│   ├── widget.cget(option) - Get single option value
│   ├── widget.keys() - Get all available options
│   └── widget.winfo_class() - Get widget class name
│
├── State Management
│   ├── widget.focus_set() - Give focus to widget
│   ├── widget.focus_get() - Get currently focused widget
│   ├── widget.grab_set() - Grab all events
│   ├── widget.grab_release() - Release event grab
│   └── widget.update() - Process pending events
│
├── Event Binding
│   ├── widget.bind(event, function) - Bind event handler
│   ├── widget.unbind(event) - Remove event binding
│   ├── widget.bind_all(event, function) - Bind to all widgets
│   └── widget.bind_class(class, event, function) - Bind to widget class
│
├── Geometry Information
│   ├── widget.winfo_width() - Get widget width
│   ├── widget.winfo_height() - Get widget height
│   ├── widget.winfo_x() - Get x position
│   ├── widget.winfo_y() - Get y position
│   ├── widget.winfo_reqwidth() - Get requested width
│   ├── widget.winfo_reqheight() - Get requested height
│   └── widget.winfo_geometry() - Get geometry string
│
└── Lifecycle
    ├── widget.destroy() - Destroy widget
    ├── widget.quit() - Quit application
    └── widget.update_idletasks() - Process idle events

SPECIFIC WIDGET METHODS:

Entry Widget:
├── entry.get() - Get text content
├── entry.set(text) - Set text content (with StringVar)
├── entry.insert(index, text) - Insert text at position
├── entry.delete(start, end) - Delete text range
├── entry.icursor(index) - Set cursor position
├── entry.select_range(start, end) - Select text range
├── entry.select_clear() - Clear selection
└── entry.xview(index) - Scroll to position

Text Widget:
├── text.get(start, end) - Get text content
├── text.insert(index, text) - Insert text at position
├── text.delete(start, end) - Delete text range
├── text.search(pattern, start, end) - Search for text
├── text.see(index) - Scroll to make index visible
├── text.mark_set(name, index) - Set named mark
├── text.mark_unset(name) - Remove named mark
├── text.tag_add(tagname, start, end) - Add tag to text range
├── text.tag_config(tagname, **options) - Configure tag
└── text.yview(action, *args) - Vertical scrolling

Listbox Widget:
├── listbox.insert(index, item) - Insert item
├── listbox.delete(start, end) - Delete items
├── listbox.get(start, end) - Get items
├── listbox.curselection() - Get selected indices
├── listbox.selection_set(start, end) - Select items
├── listbox.selection_clear() - Clear selection
├── listbox.size() - Get number of items
├── listbox.nearest(y) - Get index nearest to y coordinate
└── listbox.see(index) - Make item visible

Canvas Widget:
├── canvas.create_line(coords, **options) - Draw line
├── canvas.create_rectangle(coords, **options) - Draw rectangle
├── canvas.create_oval(coords, **options) - Draw oval/circle
├── canvas.create_polygon(coords, **options) - Draw polygon
├── canvas.create_text(x, y, **options) - Add text
├── canvas.create_image(x, y, **options) - Add image
├── canvas.create_window(x, y, **options) - Embed widget
├── canvas.coords(item, *coords) - Get/set item coordinates
├── canvas.itemconfig(item, **options) - Configure item
├── canvas.delete(item) - Delete item
├── canvas.find_all() - Get all items
├── canvas.find_closest(x, y) - Find closest item
├── canvas.move(item, dx, dy) - Move item
└── canvas.scale(item, x, y, sx, sy) - Scale item

Scale Widget:
├── scale.get() - Get current value
├── scale.set(value) - Set value
└── scale.coords() - Get slider coordinates

Scrollbar Widget:
├── scrollbar.set(first, last) - Set scrollbar position
└── scrollbar.get() - Get current position

VARIABLE CLASSES:
├── tk.StringVar() - String variable
├── tk.IntVar() - Integer variable
├── tk.DoubleVar() - Float variable
├── tk.BooleanVar() - Boolean variable
│
Variable Methods:
├── var.get() - Get variable value
├── var.set(value) - Set variable value
├── var.trace(mode, callback) - Watch for changes
└── var.trace_remove(mode, cbname) - Remove trace

DIALOG FUNCTIONS:
├── messagebox.showinfo(title, message) - Info dialog
├── messagebox.showwarning(title, message) - Warning dialog
├── messagebox.showerror(title, message) - Error dialog
├── messagebox.askquestion(title, message) - Yes/No question
├── messagebox.askyesno(title, message) - Yes/No dialog
├── messagebox.askokcancel(title, message) - OK/Cancel dialog
├── messagebox.askretrycancel(title, message) - Retry/Cancel dialog
├── filedialog.askopenfilename(**options) - Open file dialog
├── filedialog.asksaveasfilename(**options) - Save file dialog
├── filedialog.askdirectory(**options) - Directory dialog
├── filedialog.askopenfile(**options) - Open file object
└── filedialog.asksaveasfile(**options) - Save file object

COLOR FUNCTIONS:
├── root.tk.call('tk', 'chooseColor') - Color picker dialog
└── widget.winfo_rgb(color) - Convert color to RGB values

FONT FUNCTIONS:
├── font.Font(**options) - Create font object
├── font.families() - Get available font families
├── font.names() - Get named fonts
└── font_obj.measure(text) - Measure text width

IMAGE FUNCTIONS:
├── tk.PhotoImage(file=filename) - Load image file (PNG/GIF)
├── tk.BitmapImage(file=filename) - Load bitmap image
├── image.subsample(x, y) - Scale image down
├── image.zoom(x, y) - Scale image up
└── image.copy() - Copy image

GEOMETRY FUNCTIONS:
├── widget.pack_info() - Get pack options
├── widget.grid_info() - Get grid options
├── widget.place_info() - Get place options
├── widget.winfo_manager() - Get layout manager name
└── widget.winfo_geometry() - Get geometry string

CLIPBOARD FUNCTIONS:
├── root.clipboard_clear() - Clear clipboard
├── root.clipboard_append(text) - Add to clipboard
└── root.clipboard_get() - Get clipboard content

AFTER/TIMER FUNCTIONS:
├── root.after(ms, function) - Schedule function call
├── root.after_idle(function) - Call when idle
├── root.after_cancel(id) - Cancel scheduled call
└── root.update_idletasks() - Process pending events

EVENT GENERATION:
├── widget.event_generate(event) - Generate event
├── widget.event_add(virtual, sequence) - Add virtual event
└── widget.event_delete(virtual, sequence) - Remove virtual event
"""

def show_functions_reference():
    """Display the complete functions reference"""
    root = tk.Tk()
    root.title("Tkinter Functions Reference")
    root.geometry("900x700")
    
    # Create scrollable text widget
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Add scrollbar
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")
    
    # Add text widget
    text_widget = tk.Text(frame, yscrollcommand=scrollbar.set, 
                         font=("Courier", 9), wrap="none")
    text_widget.pack(side="left", fill="both", expand=True)
    
    scrollbar.config(command=text_widget.yview)
    
    # Insert the reference content
    text_widget.insert("1.0", TKINTER_FUNCTIONS_REFERENCE)
    text_widget.config(state="disabled")  # Make read-only
    
    # Add search functionality
    search_frame = tk.Frame(root)
    search_frame.pack(fill="x", padx=10, pady=5)
    
    tk.Label(search_frame, text="Search:").pack(side="left")
    search_entry = tk.Entry(search_frame, width=30)
    search_entry.pack(side="left", padx=5)
    
    def search_text():
        query = search_entry.get()
        if query:
            text_widget.config(state="normal")
            # Clear previous highlights
            text_widget.tag_remove("highlight", "1.0", "end")
            
            # Search and highlight
            start = "1.0"
            while True:
                pos = text_widget.search(query, start, "end", nocase=True)
                if not pos:
                    break
                end_pos = f"{pos}+{len(query)}c"
                text_widget.tag_add("highlight", pos, end_pos)
                start = end_pos
            
            # Configure highlight tag
            text_widget.tag_config("highlight", background="yellow", foreground="black")
            text_widget.config(state="disabled")
            
            # Scroll to first match
            first_match = text_widget.search(query, "1.0", "end", nocase=True)
            if first_match:
                text_widget.see(first_match)
    
    tk.Button(search_frame, text="Search", command=search_text).pack(side="left", padx=5)
    
    def clear_search():
        search_entry.delete(0, "end")
        text_widget.config(state="normal")
        text_widget.tag_remove("highlight", "1.0", "end")
        text_widget.config(state="disabled")
    
    tk.Button(search_frame, text="Clear", command=clear_search).pack(side="left", padx=5)
    
    # Bind Enter key to search
    search_entry.bind('<Return>', lambda e: search_text())
    
    root.mainloop()

# =====================================
# 9. VARIABLES AND DATA BINDING (moved from 8)
# =====================================

def variables_examples():
    root = tk.Tk()
    
    # StringVar - for text
    name_var = tk.StringVar()
    name_var.set("Enter your name")
    
    # IntVar - for integers
    age_var = tk.IntVar()
    age_var.set(25)
    
    # DoubleVar - for floating point numbers
    price_var = tk.DoubleVar()
    price_var.set(19.99)
    
    # BooleanVar - for checkboxes
    subscribe_var = tk.BooleanVar()
    
    # Create widgets linked to variables
    tk.Label(root, text="Name:").pack()
    name_entry = tk.Entry(root, textvariable=name_var)
    name_entry.pack(pady=5)
    
    tk.Label(root, text="Age:").pack()
    age_spinbox = tk.Spinbox(root, from_=0, to=120, textvariable=age_var)
    age_spinbox.pack(pady=5)
    
    tk.Label(root, text="Price:").pack()
    price_scale = tk.Scale(root, from_=0, to=100, resolution=0.01, 
                          orient="horizontal", variable=price_var)
    price_scale.pack(pady=5)
    
    subscribe_check = tk.Checkbutton(root, text="Subscribe to newsletter", 
                                    variable=subscribe_var)
    subscribe_check.pack(pady=5)
    
    def show_values():
        print(f"Name: {name_var.get()}")
        print(f"Age: {age_var.get()}")
        print(f"Price: {price_var.get()}")
        print(f"Subscribe: {subscribe_var.get()}")
    
    tk.Button(root, text="Show Values", command=show_values).pack(pady=10)
    
    root.mainloop()

# =====================================
# 11. COMMON PATTERNS
# =====================================

def common_patterns():
    """Common tkinter patterns and best practices"""
    
    # Pattern 1: Form layout with grid
    def create_form():
        root = tk.Tk()
        root.title("Form Example")
        
        fields = ["Name", "Email", "Phone", "Address"]
        entries = {}
        
        for i, field in enumerate(fields):
            tk.Label(root, text=f"{field}:").grid(row=i, column=0, sticky="w", padx=5, pady=5)
            entry = tk.Entry(root, width=30)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries[field] = entry
        
        def submit():
            data = {field: entry.get() for field, entry in entries.items()}
            print("Form data:", data)
        
        tk.Button(root, text="Submit", command=submit).grid(row=len(fields), column=0, columnspan=2, pady=10)
        
        root.mainloop()
    
    # Pattern 2: Menu with keyboard shortcuts
    def create_menu_app():
        root = tk.Tk()
        root.title("Menu Example")
        
        def new_file():
            print("New file")
        
        def open_file():
            print("Open file")
        
        def save_file():
            print("Save file")
        
        menubar = tk.Menu(root)
        root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        
        file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        
        # Bind keyboard shortcuts
        root.bind('<Control-n>', lambda e: new_file())
        root.bind('<Control-o>', lambda e: open_file())
        root.bind('<Control-s>', lambda e: save_file())
        
        root.mainloop()
    
    # Pattern 3: Status bar
    def create_status_bar_app():
        root = tk.Tk()
        root.title("Status Bar Example")
        
        # Main content
        text_widget = tk.Text(root)
        text_widget.pack(fill="both", expand=True)
        
        # Status bar at bottom
        status_bar = tk.Label(root, text="Ready", relief="sunken", anchor="w")
        status_bar.pack(side="bottom", fill="x")
        
        def update_status():
            cursor_pos = text_widget.index(tk.INSERT)
            line, col = cursor_pos.split('.')
            status_bar.config(text=f"Line: {line}, Column: {int(col)+1}")
        
        text_widget.bind('<KeyRelease>', lambda e: update_status())
        text_widget.bind('<ButtonRelease>', lambda e: update_status())
        
        root.mainloop()

# =====================================
# 12. QUICK REFERENCE TABLES
# =====================================

QUICK_REFERENCE = """
LAYOUT MANAGER COMPARISON:
┌─────────┬─────────────────┬─────────────────────────────────┐
│ Manager │ Best For        │ Key Options                     │
├─────────┼─────────────────┼─────────────────────────────────┤
│ pack()  │ Simple layouts  │ side, fill, expand, padx, pady  │
│ grid()  │ Form layouts    │ row, column, sticky, span       │
│ place() │ Absolute pos.   │ x, y, relx, rely, anchor        │
└─────────┴─────────────────┴─────────────────────────────────┘

COMMON WIDGET METHODS:
- widget.pack() / grid() / place() - Add to layout
- widget.config(option=value) - Change properties
- widget.get() - Get widget value (Entry, Text, etc.)
- widget.set(value) - Set widget value (StringVar, etc.)
- widget.bind(event, function) - Bind event handler
- widget.focus_set() - Give focus to widget
- widget.destroy() - Remove widget

GEOMETRY STRINGS:
- "400x300" - Width x Height
- "400x300+100+50" - Width x Height + X offset + Y offset
- "+100+50" - Just position
- "400x300" - Just size

COLOR FORMATS:
- Named: "red", "blue", "green", "white", "black"
- Hex: "#FF0000", "#00FF00", "#0000FF"
- RGB: Use hex format

FONT FORMATS:
- Tuple: ("Arial", 12, "bold")
- String: "Arial 12 bold"
- Styles: "normal", "bold", "italic", "underline"
"""

# =====================================
# MAIN CHEAT SHEET MENU
# =====================================

def main_cheat_sheet():
    root = tk.Tk()
    root.title("Tkinter Cheat Sheet")
    root.geometry("500x600")
    root.config(bg="lightblue")
    
    tk.Label(root, text="TKINTER CHEAT SHEET", 
             font=("Arial", 20, "bold"), bg="lightblue").pack(pady=20)
    
    tk.Label(root, text="Click any section to see examples:", 
             font=("Arial", 12), bg="lightblue").pack(pady=10)
    
    sections = [
        ("Basic Setup", basic_setup_example),
        ("All Widgets", widgets_reference),
        ("Pack Layout", pack_examples),
        ("Grid Layout", grid_examples),
        ("Place Layout", place_examples),
        ("Events & Bindings", events_examples),
        ("Dialogs & Messages", dialogs_examples),
        ("Styling Examples", styling_examples),
        ("Variables & Data", variables_examples),
        ("📋 Functions Reference", show_functions_reference),
    ]
    
    for section_name, section_function in sections:
        tk.Button(root, text=section_name, command=section_function,
                 font=("Arial", 11), bg="white", width=20, pady=5).pack(pady=3)
    
    # Add reference text
    text_widget = tk.Text(root, height=15, width=60, font=("Courier", 9))
    text_widget.pack(pady=20, padx=20, fill="both", expand=True)
    text_widget.insert("1.0", QUICK_REFERENCE)
    text_widget.config(state="disabled")  # Make read-only
    
    root.mainloop()

if __name__ == "__main__":
    main_cheat_sheet()
