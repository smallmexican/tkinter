# Experimental Feature - Simple To-Do List App
import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Experimental To-Do List")
        self.root.geometry("400x500")
        self.root.config(bg="lightgray")
        
        self.tasks = []
        
        # Title
        title = tk.Label(root, text="My To-Do List", 
                        font=("Arial", 18, "bold"), 
                        bg="lightgray")
        title.pack(pady=10)
        
        # Input frame
        input_frame = tk.Frame(root, bg="lightgray")
        input_frame.pack(pady=10)
        
        self.task_entry = tk.Entry(input_frame, font=("Arial", 12), width=25)
        self.task_entry.pack(side=tk.LEFT, padx=5)
        
        add_btn = tk.Button(input_frame, text="Add Task", 
                           command=self.add_task,
                           bg="lightgreen", font=("Arial", 10))
        add_btn.pack(side=tk.LEFT, padx=5)
        
        # Task listbox
        list_frame = tk.Frame(root, bg="lightgray")
        list_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox = tk.Listbox(list_frame, 
                                      yscrollcommand=scrollbar.set,
                                      font=("Arial", 11),
                                      selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.task_listbox.yview)
        
        # Button frame
        btn_frame = tk.Frame(root, bg="lightgray")
        btn_frame.pack(pady=10)
        
        complete_btn = tk.Button(btn_frame, text="Mark Complete", 
                               command=self.complete_task,
                               bg="lightblue", font=("Arial", 10))
        complete_btn.pack(side=tk.LEFT, padx=5)
        
        delete_btn = tk.Button(btn_frame, text="Delete Task", 
                             command=self.delete_task,
                             bg="lightcoral", font=("Arial", 10))
        delete_btn.pack(side=tk.LEFT, padx=5)
        
        # Bind Enter key to add task
        self.task_entry.bind('<Return>', lambda e: self.add_task())
        
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"text": task, "completed": False})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
    
    def complete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            self.tasks[index]["completed"] = True
            self.update_listbox()
            messagebox.showinfo("Success", "Task marked as complete!")
        else:
            messagebox.showwarning("Warning", "Please select a task!")
    
    def delete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            task_text = self.tasks[index]["text"]
            if messagebox.askyesno("Confirm", f"Delete task: '{task_text}'?"):
                del self.tasks[index]
                self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task!")
    
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else "○"
            display_text = f"{status} {task['text']}"
            self.task_listbox.insert(tk.END, display_text)
            
            # Color completed tasks differently
            if task["completed"]:
                self.task_listbox.itemconfig(i, {'fg': 'gray'})

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
