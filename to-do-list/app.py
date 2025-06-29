import tkinter as tk
from datetime import datetime

class Task:
    def __init__(self, task_id, text):
        self.id = task_id
        self.text = text
        self.date_created = datetime.now()
        self.date_completed = None
        self.is_completed = False
    
    def complete(self):
        """Mark the task as completed"""
        self.is_completed = True
        self.date_completed = datetime.now()
    
    def get_display_text(self):
        """Get formatted text for display in listbox"""
        return f"{self.id}: {self.text}"
    
    def get_completed_display_text(self):
        """Get formatted text for completed tasks display"""
        completed_date = self.date_completed.strftime("%m/%d/%Y %H:%M") if self.date_completed else ""
        return f"{self.text} (Completed: {completed_date})"
    
    def __str__(self):
        return self.text

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.tasks = []  # List of Task objects
        self.task_counter = 0
        self.task_var = tk.StringVar()
        self.task_var.set("Enter your task here...")  # Set example text
        self.completed_tasks = []  # List of completed Task objects
        self.root.title("My To-Do List")
        self.root.geometry("400x500")
        self.create_widgets()

    def create_widgets(self):
        # Task entry
        self.task_entry = tk.Entry(self.root, textvariable=self.task_var, font=("Arial", 14), 
                                  fg="gray", relief="flat", bd=0, highlightthickness=0,
                                  bg="#f5f5f5", insertbackground="black")
        self.task_entry.pack(pady=10, padx=10, fill=tk.X, ipady=8)
        
        # Clear example text when user clicks in the entry field
        self.task_entry.bind("<FocusIn>", self.clear_example_text)
        self.task_entry.bind("<FocusOut>", self.restore_example_text)

        # Add task button
        add_button = tk.Button(self.root, text="Add Task", command=self.add_task, 
                              font=("Arial", 14), relief="flat", bd=0,
                              bg="#4CAF50", fg="white", activebackground="#45a049")
        add_button.pack(pady=5, padx=10, fill=tk.X)
        self.add_hover_effects(add_button)

        # Task listbox
        self.task_listbox = tk.Listbox(self.root, font=("Arial", 14), selectmode=tk.SINGLE,
                                      relief="flat", bd=0, highlightthickness=0,
                                      bg="#f9f9f9", selectbackground="#4CAF50",
                                      selectforeground="white", activestyle="none")
        self.task_listbox.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)

        # Complete task button
        complete_button = tk.Button(self.root, text="Complete Task", command=self.complete_task, 
                                   font=("Arial", 14), relief="flat", bd=0,
                                   bg="#4CAF50", fg="white", activebackground="#45a049")
        complete_button.pack(pady=5, padx=10, fill=tk.X)
        self.add_hover_effects(complete_button)
        # Delete task button
        delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task,
                                 font=("Arial", 14), relief="flat", bd=0,
                                 bg="#f44336", fg="white", activebackground="#d32f2f")
        delete_button.pack(pady=5, padx=10, fill=tk.X)
        self.add_hover_effects(delete_button, hover_color="#e53935")
        
        # Clear completed tasks button
        clear_button = tk.Button(self.root, text="Clear Completed Tasks", command=self.clear_completed_tasks,
                                font=("Arial", 14), relief="flat", bd=0,
                                bg="#FF9800", fg="white", activebackground="#F57F17")
        clear_button.pack(pady=5, padx=10, fill=tk.X)
        self.add_hover_effects(clear_button, hover_color="#FB8C00")
        # Bind double-click to complete task
        self.task_listbox.bind("<Double-1>", self.complete_task)
        # Bind Enter key to add task
        self.root.bind("<Return>", lambda event: self.add_task())
        # Bind Delete key to delete task
        self.root.bind("<Delete>", lambda event: self.delete_task())
    
    def add_hover_effects(self, button, hover_color=None):
        """Add hover and click effects to buttons"""
        original_bg = button.cget("bg")
        if hover_color is None:
            hover_color = "#45a049"  # Default green hover
        
        def on_enter(e):
            button.config(bg=hover_color)
        
        def on_leave(e):
            button.config(bg=original_bg)
        
        def on_click(e):
            button.config(relief="sunken")
            button.after(100, lambda: button.config(relief="flat"))
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        button.bind("<Button-1>", on_click)
    
    def add_task(self):
        task_text = self.task_var.get().strip()
        # Don't add the example text as a task
        if task_text and task_text != "Enter your task here...":
            self.task_counter += 1
            new_task = Task(self.task_counter, task_text)
            self.tasks.append(new_task)
            self.update_task_listbox()
            self.task_var.set("Enter your task here...")  # Reset to example text
    
    def clear_example_text(self, event):
        """Clear example text when user clicks in the entry field"""
        if self.task_var.get() == "Enter your task here...":
            self.task_var.set("")
            self.task_entry.config(fg="black")  # Change text color to normal
    
    def restore_example_text(self, event):
        """Restore example text if field is empty when user clicks away"""
        if not self.task_var.get().strip():
            self.task_var.set("Enter your task here...")
            self.task_entry.config(fg="gray")  # Make example text gray
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task.get_display_text())
    
    def complete_task(self, event=None):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_text = self.task_listbox.get(selected_index)
            task_id = int(task_text.split(":")[0])
            
            # Find the task object by ID
            task_to_complete = None
            for task in self.tasks:
                if task.id == task_id:
                    task_to_complete = task
                    break
            
            if task_to_complete:
                task_to_complete.complete()
                self.completed_tasks.append(task_to_complete)
                self.tasks = [task for task in self.tasks if task.id != task_id]
                self.update_task_listbox()
                self.show_completed_tasks()
    
    def show_completed_tasks(self):
        completed_window = tk.Toplevel(self.root)
        completed_window.title("Completed Tasks")
        completed_window.geometry("400x400")
        completed_listbox = tk.Listbox(completed_window, font=("Arial", 12),
                                      relief="flat", bd=0, highlightthickness=0,
                                      bg="#f9f9f9", selectbackground="#4CAF50",
                                      selectforeground="white", activestyle="none")
        completed_listbox.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)
        for task in self.completed_tasks:
            completed_listbox.insert(tk.END, task.get_completed_display_text())
    
    def delete_task(self, event=None):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_text = self.task_listbox.get(selected_index)
            task_id = int(task_text.split(":")[0])
            self.tasks = [task for task in self.tasks if task.id != task_id]
            self.update_task_listbox()
            self.task_var.set("")
    
    def clear_completed_tasks(self):
        self.completed_tasks.clear()
        self.show_completed_tasks()
        self.update_task_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    todo_list = ToDoList(root)
    root.mainloop()