# Tkinter Cheat Sheet 🐍

A comprehensive reference guide for Python's Tkinter GUI library.

## 📋 Table of Contents
- [🛠️ Basic Setup](#️-basic-setup)
- [🎨 Main Widgets](#-main-widgets)
- [📐 Layout Managers](#-layout-managers)
- [⚙️ Widget Properties](#️-widget-properties)
- [🖱️ Events and Bindings](#️-events-and-bindings)
- [💬 Dialogs and Messages](#-dialogs-and-messages)
- [🎨 Styling and Colors](#-styling-and-colors)
- [🔗 Variables and Data Binding](#-variables-and-data-binding)
- [📚 Complete Functions Reference](#-complete-functions-reference)
- [🔧 Common Patterns](#-common-patterns)
- [📊 Quick Reference Tables](#-quick-reference-tables)
- [💡 Best Practices](#-best-practices)
- [🆘 Common Issues and Solutions](#-common-issues-and-solutions)

---

## 🛠️ Basic Setup

### Creating a Basic Window
```python
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Window Title")
root.geometry("400x300")           # width x height
root.geometry("400x300+100+50")   # width x height + x_offset + y_offset
root.resizable(False, False)      # (width_resizable, height_resizable)
root.config(bg="lightgray")       # Background color
# root.iconbitmap("icon.ico")     # Window icon (optional)

# Start the event loop
root.mainloop()
```

---

## 🎨 Main Widgets

### Label - Display Text or Images
```python
label = tk.Label(root, text="Hello World", font=("Arial", 12), 
                fg="blue", bg="white")
label.pack(pady=5)
```

### Button - Clickable Button
```python
button = tk.Button(root, text="Click Me", command=lambda: print("Clicked!"),
                  bg="lightblue", fg="black", font=("Arial", 10))
button.pack(pady=5)
```

### Entry - Single Line Text Input
```python
entry = tk.Entry(root, font=("Arial", 12), width=20)
entry.pack(pady=5)
entry.insert(0, "Default text")
```

### Text - Multi-line Text Input
```python
text = tk.Text(root, width=40, height=5, font=("Arial", 10))
text.pack(pady=5)
text.insert("1.0", "Multi-line text here")
```

### Frame - Container for Other Widgets
```python
frame = tk.Frame(root, bg="lightgray", relief="raised", bd=2)
frame.pack(pady=5, padx=10, fill="x")
```

### Checkbutton - Checkbox
```python
check_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(frame, text="Check me", variable=check_var)
checkbutton.pack(side="left")
```

### Radiobutton - Radio Button (Single Selection)
```python
radio_var = tk.StringVar()
radio1 = tk.Radiobutton(frame, text="Option 1", variable=radio_var, value="1")
radio2 = tk.Radiobutton(frame, text="Option 2", variable=radio_var, value="2")
radio1.pack(side="left")
radio2.pack(side="left")
```

### Listbox - List of Selectable Items
```python
listbox = tk.Listbox(root, height=4)
for item in ["Item 1", "Item 2", "Item 3", "Item 4"]:
    listbox.insert(tk.END, item)
listbox.pack(pady=5)
```

### Scale - Slider
```python
scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=200)
scale.pack(pady=5)
```

### Spinbox - Number Input with Up/Down Arrows
```python
spinbox = tk.Spinbox(root, from_=0, to=10, width=10)
spinbox.pack(pady=5)
```

### Canvas - Drawing Area
```python
canvas = tk.Canvas(root, width=200, height=100, bg="white")
canvas.pack(pady=5)
canvas.create_rectangle(10, 10, 50, 50, fill="red")
canvas.create_oval(60, 10, 100, 50, fill="blue")
```

### Menu - Menu Bar
```python
menubar = tk.Menu(root)
root.config(menu=menubar)
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=lambda: print("New"))
file_menu.add_command(label="Open", command=lambda: print("Open"))
```

---

## 📐 Layout Managers

### Pack - Simple Layout
```python
# Pack options:
# - side: tk.TOP, tk.BOTTOM, tk.LEFT, tk.RIGHT
# - fill: tk.X, tk.Y, tk.BOTH
# - expand: True/False
# - padx, pady: external padding
# - ipadx, ipady: internal padding

tk.Label(root, text="Top", bg="red").pack(side=tk.TOP, fill=tk.X)
tk.Label(root, text="Bottom", bg="blue").pack(side=tk.BOTTOM, fill=tk.X)
tk.Label(root, text="Left", bg="green").pack(side=tk.LEFT, fill=tk.Y)
tk.Label(root, text="Right", bg="yellow").pack(side=tk.RIGHT, fill=tk.Y)
tk.Label(root, text="Center", bg="purple").pack(expand=True)
```

### Grid - Table Layout
```python
# Grid options:
# - row, column: position in grid
# - rowspan, columnspan: span multiple cells
# - sticky: tk.N, tk.S, tk.E, tk.W (or combinations like "nsew")
# - padx, pady: padding
# - ipadx, ipady: internal padding

tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
tk.Entry(root).grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Email:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
tk.Entry(root).grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Submit").grid(row=2, column=0, columnspan=2, pady=10)
```

### Place - Absolute Positioning
```python
# Place options:
# - x, y: absolute position
# - relx, rely: relative position (0.0 to 1.0)
# - width, height: absolute size
# - relwidth, relheight: relative size
# - anchor: tk.N, tk.S, tk.E, tk.W, tk.CENTER, etc.

tk.Label(root, text="Top Left", bg="red").place(x=10, y=10)
tk.Label(root, text="Center", bg="green").place(relx=0.5, rely=0.5, anchor="center")
tk.Label(root, text="Bottom Right", bg="blue").place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
```

---

## ⚙️ Widget Properties

### Common Widget Properties

#### Visual Properties
- `bg`, `background`: Background color
- `fg`, `foreground`: Text color
- `font`: Font specification
- `relief`: "flat", "raised", "sunken", "ridge", "groove"
- `bd`, `borderwidth`: Border width
- `width`, `height`: Widget dimensions

#### Text Properties
- `text`: Display text
- `textvariable`: Link to StringVar
- `justify`: "left", "center", "right"
- `anchor`: Text position within widget
- `wraplength`: Text wrapping width

#### State Properties
- `state`: "normal", "disabled", "active"
- `cursor`: Mouse cursor when hovering

#### Layout Properties
- `padx`, `pady`: External padding
- `ipadx`, `ipady`: Internal padding
- `sticky`: Grid alignment

#### Button-specific
- `command`: Function to call when clicked
- `activebackground`: Color when pressed
- `activeforeground`: Text color when pressed

#### Entry/Text-specific
- `show`: Character to show (e.g., "*" for passwords)
- `validate`: Input validation
- `textvariable`: Link to StringVar for automatic updates

---

## 🖱️ Events and Bindings

### Common Event Patterns

#### Mouse Events
- `<Button-1>`: Left mouse button
- `<Button-2>`: Middle mouse button
- `<Button-3>`: Right mouse button
- `<Double-Button-1>`: Double click
- `<Motion>`: Mouse movement
- `<Enter>`: Mouse enters widget
- `<Leave>`: Mouse leaves widget

#### Keyboard Events
- `<KeyPress>`: Any key pressed
- `<KeyRelease>`: Any key released
- `<Return>`: Enter key
- `<BackSpace>`: Backspace key
- `<Delete>`: Delete key
- `<Tab>`: Tab key
- `<Control-c>`: Ctrl+C
- `<Alt-F4>`: Alt+F4

#### Window Events
- `<Configure>`: Window resized
- `<Destroy>`: Window closed
- `<FocusIn>`: Widget gains focus
- `<FocusOut>`: Widget loses focus

### Event Binding Example
```python
def on_click(event):
    print(f"Clicked at {event.x}, {event.y}")

def on_key_press(event):
    print(f"Key pressed: {event.keysym}")

# Bind events
label.bind("<Button-1>", on_click)        # Left click
label.bind("<Enter>", on_enter)           # Mouse enter
root.bind("<KeyPress>", on_key_press)     # Any key press
root.focus_set()  # Allow window to receive key events
```

---

## 💬 Dialogs and Messages

### Message Boxes
```python
from tkinter import messagebox

# Information dialogs
messagebox.showinfo("Info", "This is an information message")
messagebox.showwarning("Warning", "This is a warning message")
messagebox.showerror("Error", "This is an error message")

# Question dialogs
result = messagebox.askyesno("Question", "Do you want to continue?")
result = messagebox.askokcancel("Confirm", "Are you sure?")
result = messagebox.askretrycancel("Error", "Retry the operation?")
```

### File Dialogs
```python
from tkinter import filedialog

# Open file dialog
filename = filedialog.askopenfilename(
    title="Select a file",
    filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
)

# Save file dialog
filename = filedialog.asksaveasfilename(
    title="Save file as",
    defaultextension=".txt",
    filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
)

# Directory dialog
directory = filedialog.askdirectory(title="Select a directory")
```

---

## 🎨 Styling and Colors

### Color Specifications
- **Named colors**: "red", "blue", "green", "white", "black", etc.
- **Hex colors**: "#FF0000" (red), "#00FF00" (green), "#0000FF" (blue)
- **RGB colors**: Use hex format

### Font Specifications
- **Tuple format**: ("Arial", 12, "bold")
- **String format**: "Arial 12 bold"
- **Font styles**: "normal", "bold", "italic", "underline"
- **Common fonts**: "Arial", "Times", "Courier", "Helvetica"

### Relief Styles
- **"flat"**: No border (modern look)
- **"raised"**: Appears raised
- **"sunken"**: Appears pressed in
- **"ridge"**: Ridge border
- **"groove"**: Groove border

### Cursor Types
- **"arrow"**: Default cursor
- **"hand2"**: Hand pointer
- **"ibeam"**: Text cursor
- **"wait"**: Wait/hourglass
- **"crosshair"**: Crosshair
- **"question_arrow"**: Question mark

### Styling Examples
```python
# Different font styles
tk.Label(root, text="Normal Text", font=("Arial", 12))
tk.Label(root, text="Bold Text", font=("Arial", 12, "bold"))
tk.Label(root, text="Italic Text", font=("Arial", 12, "italic"))

# Different colors
tk.Label(root, text="Red Text", fg="red")
tk.Label(root, text="Blue Background", bg="#0000FF", fg="white")

# Different relief styles
tk.Label(root, text="Raised", relief="raised", bd=2, padx=10, pady=5)
tk.Label(root, text="Sunken", relief="sunken", bd=2, padx=10, pady=5)
```

---

## 🔗 Variables and Data Binding

### Variable Types
```python
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
```

### Variable Methods
- `var.get()` - Get variable value
- `var.set(value)` - Set variable value
- `var.trace(mode, callback)` - Watch for changes
- `var.trace_remove(mode, cbname)` - Remove trace

### Using Variables with Widgets
```python
# Create widgets linked to variables
name_entry = tk.Entry(root, textvariable=name_var)
age_spinbox = tk.Spinbox(root, from_=0, to=120, textvariable=age_var)
price_scale = tk.Scale(root, from_=0, to=100, variable=price_var)
subscribe_check = tk.Checkbutton(root, text="Subscribe", variable=subscribe_var)
```

---

## 📚 Complete Functions Reference

### Window/Root Methods

#### Configuration
- `root.title(string)` - Set window title
- `root.geometry(string)` - Set size/position "WIDTHxHEIGHT+X+Y"
- `root.resizable(width, height)` - Allow/disable resizing
- `root.minsize(width, height)` - Set minimum size
- `root.maxsize(width, height)` - Set maximum size
- `root.config(**options)` - Configure window properties
- `root.iconbitmap(filename)` - Set window icon
- `root.state()` - Get/set window state ("normal", "iconic", "withdrawn")

#### Control
- `root.mainloop()` - Start the event loop
- `root.quit()` - Exit the event loop
- `root.destroy()` - Destroy window and exit
- `root.withdraw()` - Hide window
- `root.deiconify()` - Show window
- `root.lift()` - Bring window to front
- `root.lower()` - Send window to back

#### Information
- `root.winfo_width()` - Get current width
- `root.winfo_height()` - Get current height
- `root.winfo_x()` - Get x position
- `root.winfo_y()` - Get y position
- `root.winfo_screenwidth()` - Get screen width
- `root.winfo_screenheight()` - Get screen height
- `root.winfo_children()` - Get child widgets

### Widget Creation Functions

#### Basic Widgets
- `tk.Label(parent, **options)` - Display text/image
- `tk.Button(parent, **options)` - Clickable button
- `tk.Entry(parent, **options)` - Single-line text input
- `tk.Text(parent, **options)` - Multi-line text input
- `tk.Frame(parent, **options)` - Container widget
- `tk.Canvas(parent, **options)` - Drawing area
- `tk.Toplevel(parent, **options)` - New window

#### Input Widgets
- `tk.Checkbutton(parent, **options)` - Checkbox
- `tk.Radiobutton(parent, **options)` - Radio button
- `tk.Scale(parent, **options)` - Slider
- `tk.Spinbox(parent, **options)` - Number input with arrows
- `tk.Listbox(parent, **options)` - List selection
- `tk.OptionMenu(parent, variable, *values)` - Dropdown menu

#### Layout Widgets
- `tk.Frame(parent, **options)` - Basic container
- `tk.LabelFrame(parent, **options)` - Frame with title
- `tk.PanedWindow(parent, **options)` - Resizable panes
- `tk.Scrollbar(parent, **options)` - Scroll control

#### Menu System
- `tk.Menu(parent, **options)` - Menu container
- `tk.Menubutton(parent, **options)` - Menu button
- `menu.add_command()` - Add menu item

### Widget Methods (Available on All Widgets)

#### Layout Management
- `widget.pack(**options)` - Pack layout manager
- `widget.grid(**options)` - Grid layout manager
- `widget.place(**options)` - Place layout manager
- `widget.pack_forget()` - Remove from pack layout
- `widget.grid_forget()` - Remove from grid layout
- `widget.place_forget()` - Remove from place layout

#### Configuration
- `widget.config(**options)` - Change widget properties
- `widget.configure(**options)` - Same as config()
- `widget.cget(option)` - Get single option value
- `widget.keys()` - Get all available options
- `widget.winfo_class()` - Get widget class name

#### State Management
- `widget.focus_set()` - Give focus to widget
- `widget.focus_get()` - Get currently focused widget
- `widget.grab_set()` - Grab all events
- `widget.grab_release()` - Release event grab
- `widget.update()` - Process pending events

#### Event Binding
- `widget.bind(event, function)` - Bind event handler
- `widget.unbind(event)` - Remove event binding
- `widget.bind_all(event, function)` - Bind to all widgets
- `widget.bind_class(class, event, function)` - Bind to widget class

### Specific Widget Methods

#### Entry Widget
- `entry.get()` - Get text content
- `entry.set(text)` - Set text content (with StringVar)
- `entry.insert(index, text)` - Insert text at position
- `entry.delete(start, end)` - Delete text range
- `entry.icursor(index)` - Set cursor position
- `entry.select_range(start, end)` - Select text range
- `entry.select_clear()` - Clear selection

#### Text Widget
- `text.get(start, end)` - Get text content
- `text.insert(index, text)` - Insert text at position
- `text.delete(start, end)` - Delete text range
- `text.search(pattern, start, end)` - Search for text
- `text.see(index)` - Scroll to make index visible
- `text.mark_set(name, index)` - Set named mark
- `text.tag_add(tagname, start, end)` - Add tag to text range
- `text.tag_config(tagname, **options)` - Configure tag

#### Listbox Widget
- `listbox.insert(index, item)` - Insert item
- `listbox.delete(start, end)` - Delete items
- `listbox.get(start, end)` - Get items
- `listbox.curselection()` - Get selected indices
- `listbox.selection_set(start, end)` - Select items
- `listbox.selection_clear()` - Clear selection
- `listbox.size()` - Get number of items

#### Canvas Widget
- `canvas.create_line(coords, **options)` - Draw line
- `canvas.create_rectangle(coords, **options)` - Draw rectangle
- `canvas.create_oval(coords, **options)` - Draw oval/circle
- `canvas.create_polygon(coords, **options)` - Draw polygon
- `canvas.create_text(x, y, **options)` - Add text
- `canvas.create_image(x, y, **options)` - Add image
- `canvas.coords(item, *coords)` - Get/set item coordinates
- `canvas.itemconfig(item, **options)` - Configure item
- `canvas.delete(item)` - Delete item
- `canvas.move(item, dx, dy)` - Move item

---

## 🔧 Common Patterns

### Form Layout with Grid
```python
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
```

### Menu with Keyboard Shortcuts
```python
def create_menu_app():
    root = tk.Tk()
    
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    
    file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
    file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
    file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
    
    # Bind keyboard shortcuts
    root.bind('<Control-n>', lambda e: new_file())
    root.bind('<Control-o>', lambda e: open_file())
    root.bind('<Control-s>', lambda e: save_file())
    
    root.mainloop()
```

### Status Bar
```python
def create_status_bar_app():
    root = tk.Tk()
    
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
```

---

## 📊 Quick Reference Tables

### Layout Manager Comparison
| Manager | Best For        | Key Options                     |
|---------|----------------|---------------------------------|
| pack()  | Simple layouts | side, fill, expand, padx, pady  |
| grid()  | Form layouts   | row, column, sticky, span       |
| place() | Absolute pos.  | x, y, relx, rely, anchor        |

### Common Widget Methods
- `widget.pack()` / `grid()` / `place()` - Add to layout
- `widget.config(option=value)` - Change properties
- `widget.get()` - Get widget value (Entry, Text, etc.)
- `widget.set(value)` - Set widget value (StringVar, etc.)
- `widget.bind(event, function)` - Bind event handler
- `widget.focus_set()` - Give focus to widget
- `widget.destroy()` - Remove widget

### Geometry Strings
- `"400x300"` - Width x Height
- `"400x300+100+50"` - Width x Height + X offset + Y offset
- `"+100+50"` - Just position
- `"400x300"` - Just size

### Color Formats
- **Named**: "red", "blue", "green", "white", "black"
- **Hex**: "#FF0000", "#00FF00", "#0000FF"
- **RGB**: Use hex format

### Font Formats
- **Tuple**: ("Arial", 12, "bold")
- **String**: "Arial 12 bold"
- **Styles**: "normal", "bold", "italic", "underline"

---

## 💡 Best Practices

### Code Organization
- Use classes to organize complex GUIs
- Separate widget creation from layout
- Use meaningful variable names
- Comment your event handlers

### Layout Tips
- Use `grid()` for form-like layouts
- Use `pack()` for simple arrangements
- Use `place()` sparingly (absolute positioning)
- Always configure grid weights for responsive design

### Event Handling
- Use lambda functions for simple callbacks
- Define separate functions for complex event handlers
- Remember to call `focus_set()` for keyboard events
- Use `bind_all()` for global shortcuts

### Performance
- Avoid creating too many widgets at once
- Use `update_idletasks()` for long operations
- Consider using `after()` for periodic updates
- Destroy unused widgets to free memory

---

## 🆘 Common Issues and Solutions

### Widget Not Showing
```python
# Problem: Widget created but not displayed
button = tk.Button(root, text="Click me")
# Solution: Add layout manager
button.pack()  # or .grid() or .place()
```

### Callback Function Issues
```python
# Problem: Lambda in loop captures wrong variable
for i in range(3):
    tk.Button(root, command=lambda: print(i)).pack()  # Always prints 2

# Solution: Use default parameter
for i in range(3):
    tk.Button(root, command=lambda x=i: print(x)).pack()  # Prints 0, 1, 2
```

### Grid/Pack Mixing
```python
# Problem: Can't mix grid() and pack() in same container
frame = tk.Frame(root)
tk.Label(frame).pack()     # Uses pack
tk.Button(frame).grid()    # Error! Can't mix with pack

# Solution: Use one layout manager per container
frame1 = tk.Frame(root)
tk.Label(frame1).pack()    # Pack in frame1

frame2 = tk.Frame(root)
tk.Button(frame2).grid()   # Grid in frame2
```

### Variable Updates Not Showing
```python
# Problem: Changing variable doesn't update widget
var = tk.StringVar()
label = tk.Label(root, text="Hello")  # Not linked to variable
var.set("New text")  # Won't update label

# Solution: Use textvariable
var = tk.StringVar()
label = tk.Label(root, textvariable=var)  # Linked to variable
var.set("New text")  # Will update label
```

---

Remember: Tkinter is included with Python, so no additional installation is required! 🎉
