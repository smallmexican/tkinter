import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Variable to store the current calculation
        self.current = ""
        self.total = 0
        
        # Create the display
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.root, bg="black")
        display_frame.pack(expand=True, fill="both", padx=10, pady=5)
        
        # Display label
        display = tk.Label(
            display_frame, 
            textvariable=self.display_var,
            font=("Arial", 20),
            bg="black",
            fg="white",
            anchor="e",
            padx=10
        )
        display.pack(expand=True, fill="both")
        
        # Button frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill="both", padx=10, pady=5)
        
        # Button configuration
        buttons = [
            ['C', '±', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '', '.', '=']
        ]
        
        # Create buttons
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                if text == '':
                    continue
                    
                # Special styling for different button types
                if text in ['C', '±', '%']:
                    bg_color = "#A6A6A6"
                    fg_color = "black"
                elif text in ['÷', '×', '-', '+', '=']:
                    bg_color = "#FF9500"
                    fg_color = "white"
                else:
                    bg_color = "#333333"
                    fg_color = "white"
                
                # Make 0 button wider
                columnspan = 2 if text == '0' else 1
                
                btn = tk.Button(
                    button_frame,
                    text=text,
                    font=("Arial", 18),
                    bg=bg_color,
                    fg=fg_color,
                    border=0,
                    command=lambda t=text: self.button_click(t)
                )
                btn.grid(row=i, column=j, columnspan=columnspan, sticky="nsew", padx=1, pady=1)
        
        # Configure grid weights for responsive design
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.grid_columnconfigure(j, weight=1)
    
    def button_click(self, char):
        if char == 'C':
            self.clear()
        elif char == '=':
            self.calculate()
        elif char == '±':
            self.plus_minus()
        elif char == '%':
            self.percentage()
        elif char in ['÷', '×', '-', '+']:
            self.operation(char)
        else:
            self.number_input(char)
    
    def clear(self):
        self.current = ""
        self.total = 0
        self.display_var.set("0")
    
    def number_input(self, char):
        if self.current == "0":
            self.current = char
        else:
            self.current += char
        self.display_var.set(self.current)
    
    def operation(self, op):
        if self.current:
            if self.total == 0:
                self.total = float(self.current)
            else:
                self.calculate()
            self.current = ""
            self.operation_pending = op
    
    def calculate(self):
        if hasattr(self, 'operation_pending') and self.current:
            try:
                current_num = float(self.current)
                
                if self.operation_pending == '+':
                    self.total += current_num
                elif self.operation_pending == '-':
                    self.total -= current_num
                elif self.operation_pending == '×':
                    self.total *= current_num
                elif self.operation_pending == '÷':
                    if current_num == 0:
                        messagebox.showerror("Error", "Cannot divide by zero!")
                        self.clear()
                        return
                    self.total /= current_num
                
                # Format the result
                if self.total == int(self.total):
                    self.display_var.set(str(int(self.total)))
                    self.current = str(int(self.total))
                else:
                    self.display_var.set(str(round(self.total, 8)))
                    self.current = str(round(self.total, 8))
                
                del self.operation_pending
                
            except ValueError:
                messagebox.showerror("Error", "Invalid input!")
                self.clear()
    
    def plus_minus(self):
        if self.current and self.current != "0":
            if self.current.startswith("-"):
                self.current = self.current[1:]
            else:
                self.current = "-" + self.current
            self.display_var.set(self.current)
    
    def percentage(self):
        if self.current:
            try:
                result = float(self.current) / 100
                if result == int(result):
                    self.current = str(int(result))
                else:
                    self.current = str(result)
                self.display_var.set(self.current)
            except ValueError:
                messagebox.showerror("Error", "Invalid input!")

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()