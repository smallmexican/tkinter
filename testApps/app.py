import tkinter as tk
from datetime import datetime


class FinanceMain:
    """Main class for the Finance Tracker application."""
    def __init__(self, root):
        self.root = root
        self.root.title("Finance Tracker")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.expenses = []  # Changed to list to store multiple expenses
        self.incomes = []   # Changed to list to store multiple incomes
        self.total_expenses = 0.0
        self.total_income = 0.0
        self.current_balance = 0.0
        self.current_frame = None  # Track current displayed frame
        self.editing_income_index = None  # Track which income is being edited
        self.editing_expense_index = None  # Track which expense is being edited
        self.create_widgets()

    def create_widgets(self):
        # Create a label
        label = tk.Label(self.root, text="Welcome to Finance Tracker", font=("Arial", 16))
        label.pack(pady=20)
        
        # Create frame as instance variable
        self.totals_frame = tk.Frame(self.root)
        self.totals_frame.pack(pady=20, fill='x', padx=20)
        
        # Now you can reference self.totals_frame anywhere in the class
        self.expenses_label = tk.Label(self.totals_frame, text=f"Total Expenses: £{self.total_expenses:.2f}", font=("Arial", 14))
        self.expenses_label.pack(side='left', padx=10, fill='x', expand=True)
        #create a label to show total income
        self.income_label = tk.Label(self.totals_frame, text=f"Total Income: £{self.total_income:.2f}", font=("Arial", 14))
        self.income_label.pack(side='left', padx=10, fill='x', expand=True)
        # create a label to show current balance
        self.balance_label = tk.Label(self.totals_frame, text=f"Current Balance: £{self.current_balance:.2f}", font=("Arial", 14))
        self.balance_label.pack(side='left', padx=10, fill='x', expand=True)
        # Create a frame for buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=20, fill='x', padx=20)
        
        # Navigation buttons
        income_button = tk.Button(self.button_frame, text="Income", command=self.show_income_frame, 
                                 font=("Arial", 12), bg="#4CAF50", fg="white", relief="flat", bd=0)
        income_button.pack(side='left', padx=5, fill='x', expand=True)
        
        expenses_button = tk.Button(self.button_frame, text="Expenses", command=self.show_expenses_frame,
                                   font=("Arial", 12), bg="#2196F3", fg="white", relief="flat", bd=0)
        expenses_button.pack(side='left', padx=5, fill='x', expand=True)
        
        charts_button = tk.Button(self.button_frame, text="Charts", command=self.show_charts_frame,
                                 font=("Arial", 12), bg="#FF9800", fg="white", relief="flat", bd=0)
        charts_button.pack(side='left', padx=5, fill='x', expand=True)
        
        # Create a main content frame where different views will be displayed
        self.content_frame = tk.Frame(self.root, bg="#f0f0f0", relief="sunken", bd=2)
        self.content_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Create canvas and scrollbar for scrollable content
        self.canvas = tk.Canvas(self.content_frame, bg="#f0f0f0", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.content_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#f0f0f0", width=600)  # Set minimum width for centering
        
        # Configure canvas scrolling and frame updates
        def on_frame_configure(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            # Also update the canvas window position when frame size changes
            canvas_width = self.canvas.winfo_width()
            frame_width = self.scrollable_frame.winfo_reqwidth()
            if canvas_width > 1:  # Make sure canvas is initialized
                x_position = max(0, (canvas_width - frame_width) // 2)
                self.canvas.coords(self.canvas_window, x_position, 0)
        
        self.scrollable_frame.bind("<Configure>", on_frame_configure)
        
        # Create the canvas window and store the window ID for later updates
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="n")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Bind canvas resize to update window position for centering
        self.canvas.bind('<Configure>', self._on_canvas_configure)
        
        # Pack canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel to canvas for better scrolling
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        
        # Show income frame by default
        self.show_income_frame()
        
        # Generate sample data for demonstration
        self.generate_sample_data()
    
    def _on_canvas_configure(self, event):
        """Handle canvas resize to center content"""
        # Update the canvas window to center the scrollable frame
        canvas_width = event.width
        frame_width = self.scrollable_frame.winfo_reqwidth()
        x_position = max(0, (canvas_width - frame_width) // 2)
        self.canvas.coords(self.canvas_window, x_position, 0)
    
    def _on_mousewheel(self, event):
        """Handle mouse wheel scrolling"""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def update_totals_display(self):
        """Update all the total labels with current values"""
        self.expenses_label.config(text=f"Total Expenses: £{self.total_expenses:.2f}")
        self.income_label.config(text=f"Total Income: £{self.total_income:.2f}")
        self.balance_label.config(text=f"Current Balance: £{self.current_balance:.2f}")
        
        # Optional: Color coding for balance
        if self.current_balance >= 0:
            self.balance_label.config(fg="green")
        else:
            self.balance_label.config(fg="red")
    
    def clear_content_frame(self):
        """Clear the current content frame"""
        if self.current_frame:
            self.current_frame.destroy()
        # Reset canvas scroll position
        self.canvas.yview_moveto(0)
    
    def show_income_frame(self):
        """Display the income management frame"""
        self.clear_content_frame()
        self.current_frame = tk.Frame(self.scrollable_frame, bg="#f0f0f0")
        self.current_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Income frame title
        title_label = tk.Label(self.current_frame, text="Income Management", 
                              font=("Arial", 16, "bold"), bg="#f0f0f0")
        title_label.pack(pady=10)
        
        # Income entry form
        entry_frame = tk.Frame(self.current_frame, bg="#f0f0f0")
        entry_frame.pack(pady=10, fill='x')
        
        # Create a centered container for the form
        form_container = tk.Frame(entry_frame, bg="#f0f0f0")
        form_container.pack(expand=True)
        
        tk.Label(form_container, text="Amount (£):", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, sticky='e', padx=(0, 10), pady=5)
        self.income_amount_entry = tk.Entry(form_container, font=("Arial", 12), width=25)
        self.income_amount_entry.grid(row=0, column=1, padx=(0, 0), pady=5, sticky='w')
        
        tk.Label(form_container, text="Description:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, sticky='e', padx=(0, 10), pady=5)
        self.income_desc_entry = tk.Entry(form_container, font=("Arial", 12), width=25)
        self.income_desc_entry.grid(row=1, column=1, padx=(0, 0), pady=5, sticky='w')
        
        # Buttons container frame for centering buttons
        buttons_container = tk.Frame(self.current_frame, bg="#f0f0f0")
        buttons_container.pack(pady=10, expand=True)
        
        # Add income button
        add_income_btn = tk.Button(buttons_container, text="Add Income", 
                                  command=self.add_income_from_form,
                                  font=("Arial", 12), bg="#4CAF50", fg="white", relief="flat", bd=0)
        add_income_btn.pack(pady=5)
        
        # Edit income button
        edit_income_btn = tk.Button(buttons_container, text="Edit Selected Income", 
                                   command=self.edit_income_from_list,
                                   font=("Arial", 12), bg="#FF9800", fg="white", relief="flat", bd=0)
        edit_income_btn.pack(pady=5)
        
        # Delete income button
        delete_income_btn = tk.Button(buttons_container, text="Delete Selected Income", 
                                     command=self.delete_income_from_list,
                                     font=("Arial", 12), bg="#f44336", fg="white", relief="flat", bd=0)
        delete_income_btn.pack(pady=5)
        
        # Income history section container for centering
        history_container = tk.Frame(self.current_frame, bg="#f0f0f0")
        history_container.pack(pady=(20, 0), expand=True, fill='both')
        
        history_label = tk.Label(history_container, text="Income History:", 
                                font=("Arial", 14, "bold"), bg="#f0f0f0")
        history_label.pack(pady=(0, 5))
        
        self.income_listbox = tk.Listbox(history_container, font=("Arial", 10), height=8)
        self.income_listbox.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Refresh the income list
        self.refresh_income_list()
    
    def show_expenses_frame(self):
        """Display the expenses management frame"""
        self.clear_content_frame()
        self.current_frame = tk.Frame(self.scrollable_frame, bg="#f0f0f0")
        self.current_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Expenses frame title
        title_label = tk.Label(self.current_frame, text="Expense Management", 
                              font=("Arial", 16, "bold"), bg="#f0f0f0")
        title_label.pack(pady=10)
        
        # Expense entry form
        entry_frame = tk.Frame(self.current_frame, bg="#f0f0f0")
        entry_frame.pack(pady=10, fill='x')
        
        # Create a centered container for the form
        form_container = tk.Frame(entry_frame, bg="#f0f0f0")
        form_container.pack(expand=True)
        
        tk.Label(form_container, text="Amount (£):", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, sticky='e', padx=(0, 10), pady=5)
        self.expense_amount_entry = tk.Entry(form_container, font=("Arial", 12), width=25)
        self.expense_amount_entry.grid(row=0, column=1, padx=(0, 0), pady=5, sticky='w')
        
        tk.Label(form_container, text="Description:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, sticky='e', padx=(0, 10), pady=5)
        self.expense_desc_entry = tk.Entry(form_container, font=("Arial", 12), width=25)
        self.expense_desc_entry.grid(row=1, column=1, padx=(0, 0), pady=5, sticky='w')
        
        tk.Label(form_container, text="Category:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, sticky='e', padx=(0, 10), pady=5)
        self.expense_category_var = tk.StringVar(value="Food")
        category_options = ["Food", "Transportation", "Housing", "Entertainment", "Healthcare", "Other"]
        self.expense_category_menu = tk.OptionMenu(form_container, self.expense_category_var, *category_options)
        self.expense_category_menu.config(width=20)
        self.expense_category_menu.grid(row=2, column=1, padx=(0, 0), pady=5, sticky='w')
        
        # Buttons container frame for centering buttons
        buttons_container = tk.Frame(self.current_frame, bg="#f0f0f0")
        buttons_container.pack(pady=10, expand=True)
        
        # Add expense button
        add_expense_btn = tk.Button(buttons_container, text="Add Expense", 
                                   command=self.add_expense_from_form,
                                   font=("Arial", 12), bg="#2196F3", fg="white", relief="flat", bd=0)
        add_expense_btn.pack(pady=5)
        
        # Edit expense button
        edit_expense_btn = tk.Button(buttons_container, text="Edit Selected Expense", 
                                    command=self.edit_expense_from_list,
                                    font=("Arial", 12), bg="#FF9800", fg="white", relief="flat", bd=0)
        edit_expense_btn.pack(pady=5)
        
        # Delete expense button
        delete_expense_btn = tk.Button(buttons_container, text="Delete Selected Expense", 
                                      command=self.delete_expense_from_list,
                                      font=("Arial", 12), bg="#f44336", fg="white", relief="flat", bd=0)
        delete_expense_btn.pack(pady=5)
        
        # Expense history section container for centering
        history_container = tk.Frame(self.current_frame, bg="#f0f0f0")
        history_container.pack(pady=(20, 0), expand=True, fill='both')
        
        # Expense history listbox
        history_label = tk.Label(history_container, text="Expense History:", 
                                font=("Arial", 14, "bold"), bg="#f0f0f0")
        history_label.pack(pady=(0, 5))
        
        self.expense_listbox = tk.Listbox(history_container, font=("Arial", 10), height=8)
        self.expense_listbox.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Refresh the expense list
        self.refresh_expense_list()
    
    def show_charts_frame(self):
        """Display the charts and summary frame"""
        self.clear_content_frame()
        self.current_frame = tk.Frame(self.scrollable_frame, bg="#f0f0f0")
        self.current_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Main container for centering all content
        main_container = tk.Frame(self.current_frame, bg="#f0f0f0")
        main_container.pack(expand=True, fill='both')
        
        # Charts frame title
        title_label = tk.Label(main_container, text="Financial Summary & Charts", 
                              font=("Arial", 16, "bold"), bg="#f0f0f0")
        title_label.pack(pady=10)
        
        # Time period selector
        period_container = tk.Frame(main_container, bg="#f0f0f0")
        period_container.pack(pady=10)
        
        tk.Label(period_container, text="View by:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(side='left', padx=(0, 10))
        
        self.chart_period_var = tk.StringVar(value="Week")
        period_options = ["Day", "Week", "Month"]
        
        for period in period_options:
            rb = tk.Radiobutton(period_container, text=period, variable=self.chart_period_var, 
                               value=period, bg="#f0f0f0", font=("Arial", 11),
                               command=self.update_chart_display)
            rb.pack(side='left', padx=5)
        
        # Navigation controls
        nav_container = tk.Frame(main_container, bg="#f0f0f0")
        nav_container.pack(pady=10)
        
        # Initialize chart offset (0 = current period, 1 = previous period, etc.)
        if not hasattr(self, 'chart_offset'):
            self.chart_offset = 0
        
        prev_btn = tk.Button(nav_container, text="← Previous", 
                            command=self.show_previous_period,
                            font=("Arial", 10), bg="#2196F3", fg="white", relief="flat", bd=0)
        prev_btn.pack(side='left', padx=5)
        
        self.period_label = tk.Label(nav_container, text="", font=("Arial", 11, "bold"), bg="#f0f0f0")
        self.period_label.pack(side='left', padx=15)
        
        next_btn = tk.Button(nav_container, text="Next →", 
                            command=self.show_next_period,
                            font=("Arial", 10), bg="#2196F3", fg="white", relief="flat", bd=0)
        next_btn.pack(side='left', padx=5)
        
        # Chart container
        self.chart_container = tk.Frame(main_container, bg="#f0f0f0")
        self.chart_container.pack(pady=20, fill='x')
        
        # Create the bar chart
        self.create_simple_bar_chart(self.chart_container)
        
        # Initialize period label
        if hasattr(self, 'period_label'):
            period_text = self.get_period_label(self.chart_period_var.get(), self.chart_offset)
            self.period_label.config(text=period_text)
        
        # Summary statistics container
        summary_container = tk.Frame(main_container, bg="#f0f0f0")
        summary_container.pack(pady=20, expand=True)
        
        # Summary statistics frame
        summary_frame = tk.Frame(summary_container, bg="#f0f0f0")
        summary_frame.pack()
        
        tk.Label(summary_frame, text=f"Total Transactions: {len(self.incomes) + len(self.expenses)}", 
                font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        tk.Label(summary_frame, text=f"Income Entries: {len(self.incomes)}", 
                font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        tk.Label(summary_frame, text=f"Expense Entries: {len(self.expenses)}", 
                font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        
        # Category breakdown (simple text-based for now)
        if self.expenses:
            # Category container for centering
            category_container = tk.Frame(main_container, bg="#f0f0f0")
            category_container.pack(pady=20, expand=True)
            
            category_frame = tk.Frame(category_container, bg="#f0f0f0")
            category_frame.pack()
            
            category_label = tk.Label(category_frame, text="Expense Categories:", 
                                     font=("Arial", 14, "bold"), bg="#f0f0f0")
            category_label.pack(pady=(0, 10))
            
            categories = {}
            for expense in self.expenses:
                cat = expense['category']
                categories[cat] = categories.get(cat, 0) + expense['amount']
            
            for category, amount in categories.items():
                percentage = (amount / self.total_expenses) * 100 if self.total_expenses > 0 else 0
                cat_text = f"{category}: £{amount:.2f} ({percentage:.1f}%)"
                tk.Label(category_frame, text=cat_text, font=("Arial", 11), bg="#f0f0f0").pack(pady=2)
    
    def add_income_from_form(self):
        """Add income from the form inputs"""
        try:
            amount = float(self.income_amount_entry.get())
            description = self.income_desc_entry.get().strip()
            
            if not description:
                raise ValueError("Description is required")
            
            self.add_income(amount, description)
            
            # Clear the form
            self.income_amount_entry.delete(0, tk.END)
            self.income_desc_entry.delete(0, tk.END)
            
            # Refresh the list
            self.refresh_income_list()
            
        except ValueError as e:
            # Simple error handling - you could improve this with a popup
            print(f"Error: {e}")
    
    def edit_income_from_list(self):
        """Edit selected income from the list"""
        try:
            selected_index = self.income_listbox.curselection()
            if not selected_index:
                print("Please select an income entry to edit")
                return
            
            index = selected_index[0]
            income = self.incomes[index]
            
            # Pre-fill the form with existing data
            self.income_amount_entry.delete(0, tk.END)
            self.income_amount_entry.insert(0, str(income['amount']))
            
            self.income_desc_entry.delete(0, tk.END)
            self.income_desc_entry.insert(0, income['description'])
            
            # Store the index for updating
            self.editing_income_index = index
            
            # Change the Add button text to indicate editing mode
            for widget in self.current_frame.winfo_children():
                if isinstance(widget, tk.Button) and widget['text'] == 'Add Income':
                    widget.config(text='Update Income', command=self.update_income_from_form)
                    break
            
        except Exception as e:
            print(f"Error editing income: {e}")
    
    def update_income_from_form(self):
        """Update the income being edited"""
        try:
            amount = float(self.income_amount_entry.get())
            description = self.income_desc_entry.get().strip()
            
            if not description:
                raise ValueError("Description is required")
            
            if amount <= 0:
                raise ValueError("Amount must be positive")
            
            # Update totals by removing old amount and adding new
            old_income = self.incomes[self.editing_income_index]
            self.total_income -= old_income['amount']
            self.current_balance -= old_income['amount']  # Remove old amount from balance
            
            # Update the income entry
            self.incomes[self.editing_income_index] = {
                "description": description,
                "amount": amount,
                "date": old_income['date']  # Keep original date
            }
            
            # Update totals with new amount
            self.total_income += amount
            self.current_balance += amount  # Add new amount to balance
            self.update_totals_display()
            
            # Clear the form and reset button
            self.income_amount_entry.delete(0, tk.END)
            self.income_desc_entry.delete(0, tk.END)
            
            # Reset the button back to Add mode
            for widget in self.current_frame.winfo_children():
                if isinstance(widget, tk.Button) and widget['text'] == 'Update Income':
                    widget.config(text='Add Income', command=self.add_income_from_form)
                    break
            
            # Clear editing index
            self.editing_income_index = None
            
            # Refresh the list
            self.refresh_income_list()
            
            print(f"Income updated: {description} - £{amount}")
            
        except ValueError as e:
            print(f"Error: {e}")
    
    def delete_income_from_list(self):
        """Delete selected income from the list"""
        try:
            selected_index = self.income_listbox.curselection()
            if not selected_index:
                print("Please select an income entry to delete")
                return
            
            index = selected_index[0]
            income = self.incomes[index]
            
            # Update totals
            self.total_income -= income['amount']
            self.current_balance -= income['amount']
            
            # Remove from list
            del self.incomes[index]
            
            # Update display
            self.update_totals_display()
            self.refresh_income_list()
            
            print(f"Income deleted: {income['description']} - £{income['amount']}")
            
        except Exception as e:
            print(f"Error deleting income: {e}")
    
    def add_expense_from_form(self):
        """Add expense from the form inputs"""
        try:
            amount = float(self.expense_amount_entry.get())
            description = self.expense_desc_entry.get().strip()
            category = self.expense_category_var.get()
            
            if not description:
                raise ValueError("Description is required")
            
            self.add_expense(amount, description, category)
            
            # Clear the form
            self.expense_amount_entry.delete(0, tk.END)
            self.expense_desc_entry.delete(0, tk.END)
            
            # Refresh the list
            self.refresh_expense_list()
            
        except ValueError as e:
            # Simple error handling - you could improve this with a popup
            print(f"Error: {e}")
    
    def edit_expense_from_list(self):
        """Edit selected expense from the list"""
        try:
            selected_index = self.expense_listbox.curselection()
            if not selected_index:
                print("Please select an expense entry to edit")
                return
            
            index = selected_index[0]
            expense = self.expenses[index]
            
            # Pre-fill the form with existing data
            self.expense_amount_entry.delete(0, tk.END)
            self.expense_amount_entry.insert(0, str(expense['amount']))
            
            self.expense_desc_entry.delete(0, tk.END)
            self.expense_desc_entry.insert(0, expense['description'])
            
            self.expense_category_var.set(expense['category'])
            
            # Store the index for updating
            self.editing_expense_index = index
            
            # Change the Add button text to indicate editing mode
            for widget in self.current_frame.winfo_children():
                if isinstance(widget, tk.Button) and widget['text'] == 'Add Expense':
                    widget.config(text='Update Expense', command=self.update_expense_from_form)
                    break
            
        except Exception as e:
            print(f"Error editing expense: {e}")
    
    def update_expense_from_form(self):
        """Update the expense being edited"""
        try:
            amount = float(self.expense_amount_entry.get())
            description = self.expense_desc_entry.get().strip()
            category = self.expense_category_var.get()
            
            if not description:
                raise ValueError("Description is required")
            
            if amount <= 0:
                raise ValueError("Amount must be positive")
            
            # Update totals by removing old amount and adding new
            old_expense = self.expenses[self.editing_expense_index]
            self.total_expenses -= old_expense['amount']
            self.current_balance += old_expense['amount']  # Add old amount back to balance (since it was subtracted)
            
            # Update the expense entry
            self.expenses[self.editing_expense_index] = {
                "description": description,
                "amount": amount,
                "category": category,
                "date": old_expense['date']  # Keep original date
            }
            
            # Update totals with new amount
            self.total_expenses += amount
            self.current_balance -= amount  # Subtract new amount from balance
            self.update_totals_display()
            
            # Clear the form and reset button
            self.expense_amount_entry.delete(0, tk.END)
            self.expense_desc_entry.delete(0, tk.END)
            
            # Reset the button back to Add mode
            for widget in self.current_frame.winfo_children():
                if isinstance(widget, tk.Button) and widget['text'] == 'Update Expense':
                    widget.config(text='Add Expense', command=self.add_expense_from_form)
                    break
            
            # Clear editing index
            self.editing_expense_index = None
            
            # Refresh the list
            self.refresh_expense_list()
            
            print(f"Expense updated: {description} - £{amount} ({category})")
            
        except ValueError as e:
            print(f"Error: {e}")
    
    def delete_expense_from_list(self):
        """Delete selected expense from the list"""
        try:
            selected_index = self.expense_listbox.curselection()
            if not selected_index:
                print("Please select an expense entry to delete")
                return
            
            index = selected_index[0]
            expense = self.expenses[index]
            
            # Update totals
            self.total_expenses -= expense['amount']
            self.current_balance += expense['amount']  # Add back to balance
            
            # Remove from list
            del self.expenses[index]
            
            # Update display
            self.update_totals_display()
            self.refresh_expense_list()
            
            print(f"Expense deleted: {expense['description']} - £{expense['amount']} ({expense['category']})")
            
        except Exception as e:
            print(f"Error deleting expense: {e}")
    
    def refresh_income_list(self):
        """Refresh the income history listbox"""
        if hasattr(self, 'income_listbox'):
            self.income_listbox.delete(0, tk.END)
            for income in self.incomes:
                date_str = income['date'].strftime("%m/%d/%Y %H:%M")
                text = f"£{income['amount']:.2f} - {income['description']} ({date_str})"
                self.income_listbox.insert(tk.END, text)
    
    def refresh_expense_list(self):
        """Refresh the expense history listbox"""
        if hasattr(self, 'expense_listbox'):
            self.expense_listbox.delete(0, tk.END)
            for expense in self.expenses:
                date_str = expense['date'].strftime("%m/%d/%Y %H:%M")
                text = f"£{expense['amount']:.2f} - {expense['description']} ({expense['category']}) ({date_str})"
                self.expense_listbox.insert(tk.END, text)
    
    def add_expense(self, amount, description, category):
        """Add an expense to the tracker."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        expense = {
            "description": description,
            "category": category,
            "amount": amount,
            "date": datetime.now()
        }
        
        self.expenses.append(expense)
        self.total_expenses += amount
        self.current_balance -= amount
        self.update_totals_display()  # Update the labels!
        print(f"Expense added: {description} - £{amount} ({category}) on {expense['date']}")

    def add_income(self, amount, description):
        """Add an income to the tracker."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        income = {
            "description": description,
            "amount": amount,
            "date": datetime.now()
        }
        
        self.incomes.append(income)
        self.total_income += amount
        self.current_balance += amount
        self.update_totals_display()  # Update the labels!
        print(f"Income added: {description} - £{amount} on {income['date']}")

    def update_chart_display(self):
        """Update the chart when period selection changes"""
        if hasattr(self, 'chart_canvas'):
            self.chart_canvas.destroy()
        
        # Update period label if it exists
        if hasattr(self, 'period_label'):
            period_text = self.get_period_label(self.chart_period_var.get(), self.chart_offset)
            self.period_label.config(text=period_text)
        
        # Clear and recreate chart in the container
        if hasattr(self, 'chart_container'):
            for widget in self.chart_container.winfo_children():
                widget.destroy()
            self.create_simple_bar_chart(self.chart_container)
        
        # Update the period label
        if hasattr(self, 'period_label') and self.chart_period_var.get():
            current_period = self.get_period_label(self.chart_period_var.get(), self.chart_offset)
            self.period_label.config(text=current_period)
    
    def show_previous_period(self):
        """Show previous time period in chart"""
        self.chart_offset += 1
        self.update_chart_display()
    
    def show_next_period(self):
        """Show next time period in chart"""
        if self.chart_offset > 0:
            self.chart_offset -= 1
            self.update_chart_display()
    
    def get_period_label(self, period_type, offset):
        """Get a descriptive label for the current period being displayed"""
        from datetime import date, timedelta
        import calendar
        
        today = date.today()
        
        if period_type == "Day":
            start_date = today - timedelta(days=(offset * 7) + 6)
            end_date = today - timedelta(days=offset * 7)
            return f"{start_date.strftime('%m/%d')} - {end_date.strftime('%m/%d/%Y')}"
        
        elif period_type == "Week":
            start_week = today - timedelta(days=today.weekday() + (offset * 4 * 7) + (3 * 7))
            end_week = today - timedelta(days=today.weekday() + (offset * 4 * 7))
            return f"{start_week.strftime('%m/%d')} - {end_week.strftime('%m/%d/%Y')}"
        
        elif period_type == "Month":
            start_month_offset = offset * 6 + 5
            end_month_offset = offset * 6
            
            if today.month - start_month_offset > 0:
                start_month = today.month - start_month_offset
                start_year = today.year
            else:
                start_month = 12 + (today.month - start_month_offset)
                start_year = today.year - ((start_month_offset - today.month) // 12 + 1)
            
            if today.month - end_month_offset > 0:
                end_month = today.month - end_month_offset
                end_year = today.year
            else:
                end_month = 12 + (today.month - end_month_offset)
                end_year = today.year - ((end_month_offset - today.month) // 12 + 1)
            
            start_name = calendar.month_abbr[start_month]
            end_name = calendar.month_abbr[end_month]
            
            if start_year == end_year:
                return f"{start_name} - {end_name} {end_year}"
            else:
                return f"{start_name} {end_year} - {end_name} {end_year}"
        
        return ""
    
    def create_simple_bar_chart(self, parent):
        """Create a simple bar chart showing income vs expenses"""
        chart_frame = tk.Frame(parent, bg="#f0f0f0")
        chart_frame.pack(pady=10)
        
        # Chart title
        chart_title = tk.Label(chart_frame, text=f"Income vs Expenses ({self.chart_period_var.get()}ly)", 
                              font=("Arial", 14, "bold"), bg="#f0f0f0")
        chart_title.pack(pady=(0, 10))
        
        # Get data for the selected period
        chart_data = self.get_chart_data(self.chart_period_var.get())
        
        if not chart_data:
            no_data_label = tk.Label(chart_frame, text="No data available for the selected period", 
                                   font=("Arial", 12), bg="#f0f0f0", fg="gray")
            no_data_label.pack(pady=20)
            return
        
        # Create canvas for chart
        self.chart_canvas = tk.Canvas(chart_frame, width=600, height=300, bg="white", relief="ridge", bd=2)
        self.chart_canvas.pack(pady=10)
        
        # Chart dimensions
        chart_width = 550
        chart_height = 250
        margin_left = 50
        margin_bottom = 30
        margin_top = 20
        
        # Find max value for scaling
        max_value = 0
        for period, data in chart_data.items():
            max_value = max(max_value, data['income'], data['expenses'])
        
        if max_value == 0:
            max_value = 100  # Prevent division by zero
        
        # Calculate bar dimensions
        bar_width = chart_width // (len(chart_data) * 2 + 1)
        if bar_width < 20:
            bar_width = 20
        
        # Draw chart
        x_pos = margin_left
        for i, (period, data) in enumerate(chart_data.items()):
            # Calculate bar heights
            income_height = (data['income'] / max_value) * chart_height
            expense_height = (data['expenses'] / max_value) * chart_height
            
            # Draw income bar (green)
            self.chart_canvas.create_rectangle(
                x_pos, chart_height + margin_top - income_height,
                x_pos + bar_width, chart_height + margin_top,
                fill="#4CAF50", outline="#2E7D32"
            )
            
            # Draw expense bar (red)
            self.chart_canvas.create_rectangle(
                x_pos + bar_width + 5, chart_height + margin_top - expense_height,
                x_pos + (bar_width * 2) + 5, chart_height + margin_top,
                fill="#f44336", outline="#c62828"
            )
            
            # Add period label
            label_x = x_pos + bar_width
            self.chart_canvas.create_text(
                label_x, chart_height + margin_top + 15,
                text=period, font=("Arial", 9), anchor="n"
            )
            
            # Add value labels
            if income_height > 20:
                self.chart_canvas.create_text(
                    x_pos + bar_width//2, chart_height + margin_top - income_height//2,
                    text=f"£{data['income']:.0f}", font=("Arial", 8), fill="white"
                )
            
            if expense_height > 20:
                self.chart_canvas.create_text(
                    x_pos + bar_width + bar_width//2 + 5, chart_height + margin_top - expense_height//2,
                    text=f"£{data['expenses']:.0f}", font=("Arial", 8), fill="white"
                )
            
            x_pos += bar_width * 2 + 20
        
        # Add legend
        legend_frame = tk.Frame(chart_frame, bg="#f0f0f0")
        legend_frame.pack(pady=5)
        
        # Income legend
        income_color = tk.Frame(legend_frame, bg="#4CAF50", width=15, height=15)
        income_color.pack(side='left', padx=(0, 5))
        tk.Label(legend_frame, text="Income", font=("Arial", 10), bg="#f0f0f0").pack(side='left', padx=(0, 15))
        
        # Expense legend
        expense_color = tk.Frame(legend_frame, bg="#f44336", width=15, height=15)
        expense_color.pack(side='left', padx=(0, 5))
        tk.Label(legend_frame, text="Expenses", font=("Arial", 10), bg="#f0f0f0").pack(side='left')
    
    def get_chart_data(self, period_type):
        """Get aggregated data for the chart based on period type and offset"""
        from datetime import timedelta, date
        import calendar
        
        if not self.incomes and not self.expenses:
            return {}
        
        chart_data = {}
        today = date.today()
        
        if period_type == "Day":
            # Show 7 days starting from offset weeks ago
            base_date = today - timedelta(days=self.chart_offset * 7)
            for i in range(6, -1, -1):
                target_date = base_date - timedelta(days=i)
                day_key = target_date.strftime("%m/%d")
                chart_data[day_key] = {'income': 0, 'expenses': 0}
                
                # Sum incomes for this day
                for income in self.incomes:
                    if income['date'].date() == target_date:
                        chart_data[day_key]['income'] += income['amount']
                
                # Sum expenses for this day
                for expense in self.expenses:
                    if expense['date'].date() == target_date:
                        chart_data[day_key]['expenses'] += expense['amount']
        
        elif period_type == "Week":
            # Show 4 weeks starting from offset*4 weeks ago
            base_date = today - timedelta(days=today.weekday() + (self.chart_offset * 4 * 7))
            for i in range(3, -1, -1):
                week_start = base_date - timedelta(days=i * 7)
                week_end = week_start + timedelta(days=6)
                week_key = f"Week {week_start.strftime('%m/%d')}"
                chart_data[week_key] = {'income': 0, 'expenses': 0}
                
                # Sum incomes for this week
                for income in self.incomes:
                    if week_start <= income['date'].date() <= week_end:
                        chart_data[week_key]['income'] += income['amount']
                
                # Sum expenses for this week
                for expense in self.expenses:
                    if week_start <= expense['date'].date() <= week_end:
                        chart_data[week_key]['expenses'] += expense['amount']
        
        elif period_type == "Month":
            # Show 6 months starting from offset*6 months ago
            for i in range(5, -1, -1):
                month_offset = (self.chart_offset * 6) + i
                if today.month - month_offset > 0:
                    target_month = today.month - month_offset
                    target_year = today.year
                else:
                    years_back = ((month_offset - today.month) // 12) + 1
                    target_month = 12 - ((month_offset - today.month) % 12)
                    if target_month == 12 and (month_offset - today.month) % 12 == 0:
                        target_month = today.month
                        years_back -= 1
                    target_year = today.year - years_back
                
                month_key = calendar.month_abbr[target_month]
                chart_data[month_key] = {'income': 0, 'expenses': 0}
                
                # Sum incomes for this month
                for income in self.incomes:
                    if (income['date'].month == target_month and 
                        income['date'].year == target_year):
                        chart_data[month_key]['income'] += income['amount']
                
                # Sum expenses for this month
                for expense in self.expenses:
                    if (expense['date'].month == target_month and 
                        expense['date'].year == target_year):
                        chart_data[month_key]['expenses'] += expense['amount']
        
        return chart_data
    
    def generate_sample_data(self):
        """Generate sample data for testing - 3 months of financial data"""
        from datetime import datetime, timedelta
        import random
        
        # Clear existing data
        self.expenses = []
        self.incomes = []
        self.total_expenses = 0.0
        self.total_income = 0.0
        self.current_balance = 0.0
        
        # Define expense categories and typical amounts
        expense_categories = {
            "Food": [15, 25, 35, 45, 8, 12, 20, 30, 18, 22],
            "Transportation": [45, 60, 25, 30, 15, 20, 85, 95],
            "Housing": [800, 120, 150, 80, 95],
            "Entertainment": [25, 35, 15, 45, 20, 30, 40, 18],
            "Healthcare": [85, 120, 45, 65, 200, 150],
            "Other": [20, 35, 50, 15, 25, 40, 30]
        }
        
        # Generate data for last 3 months including current month
        today = datetime.now()
        
        for month_offset in range(2, -1, -1):  # 2 months ago to current month
            # Calculate target month
            target_date = today - timedelta(days=month_offset * 30)
            year = target_date.year
            month = target_date.month
            
            # For current month, don't go past today
            max_day = min(28, today.day if month_offset == 0 else 28)
            
            # Add monthly salary (always on the 1st of the month)
            salary_date = datetime(year, month, 1, 9, 0, 0)
            salary_income = {
                "description": "Monthly Salary",
                "amount": 2700.0,
                "date": salary_date
            }
            self.incomes.append(salary_income)
            self.total_income += 2700.0
            self.current_balance += 2700.0
            
            # Add occasional freelance income
            if random.random() < 0.3:  # 30% chance of freelance income
                freelance_day = random.randint(5, 25)
                freelance_date = datetime(year, month, freelance_day, 
                                        random.randint(10, 16), random.randint(0, 59), 0)
                freelance_amount = random.randint(200, 800)
                freelance_income = {
                    "description": "Freelance Work",
                    "amount": float(freelance_amount),
                    "date": freelance_date
                }
                self.incomes.append(freelance_income)
                self.total_income += freelance_amount
                self.current_balance += freelance_amount
            
            # Generate 20-25 expenses for this month
            num_expenses = random.randint(20, 25)
            
            for i in range(num_expenses):
                # Random day of the month (respect max_day for current month)
                day = random.randint(1, max_day)
                hour = random.randint(8, 22)
                minute = random.randint(0, 59)
                expense_date = datetime(year, month, day, hour, minute, 0)
                
                # Random category and amount
                category = random.choice(list(expense_categories.keys()))
                base_amount = random.choice(expense_categories[category])
                
                # Add some variation to the amount
                variation = random.uniform(0.8, 1.3)
                amount = round(base_amount * variation, 2)
                
                # Generate description based on category
                descriptions = {
                    "Food": ["Groceries", "Restaurant", "Coffee", "Lunch", "Dinner", "Snacks", "Takeaway"],
                    "Transportation": ["Gas", "Bus fare", "Taxi", "Parking", "Car maintenance", "Train ticket"],
                    "Housing": ["Rent", "Utilities", "Internet", "Phone", "Home supplies", "Repairs"],
                    "Entertainment": ["Movie", "Concert", "Games", "Books", "Streaming", "Sports"],
                    "Healthcare": ["Pharmacy", "Doctor visit", "Dentist", "Gym", "Vitamins"],
                    "Other": ["Clothing", "Gifts", "Personal care", "Electronics", "Miscellaneous"]
                }
                
                description = random.choice(descriptions[category])
                
                # Create expense entry
                expense = {
                    "description": description,
                    "category": category,
                    "amount": amount,
                    "date": expense_date
                }
                
                self.expenses.append(expense)
                self.total_expenses += amount
                self.current_balance -= amount
        
        # Sort entries by date for better organization
        self.incomes.sort(key=lambda x: x['date'])
        self.expenses.sort(key=lambda x: x['date'])
        
        # Update display
        self.update_totals_display()
        print(f"Sample data generated:")
        print(f"- {len(self.incomes)} income entries")
        print(f"- {len(self.expenses)} expense entries")
        print(f"- Total Income: £{self.total_income:.2f}")
        print(f"- Total Expenses: £{self.total_expenses:.2f}")
        print(f"- Current Balance: £{self.current_balance:.2f}")
    
    def start_tracking(self):
        print("Tracking started...")
        # Sample data is now generated automatically in generate_sample_data()

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceMain(root)
    root.mainloop()