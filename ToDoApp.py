import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to remove!")

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x300")
root.configure(bg="purple")

# Widgets
heading = tk.Label(root, text="To-Do List: Add Task", font=("Times roman", 18, "bold"), width=25)
task_entry = tk.Entry(root, width=30)
add_button = tk.Button(root, text="Add", command=add_task)
remove_button = tk.Button(root, text="Remove", command=remove_task)
task_list = tk.Listbox(root, width=40, height=6)

# Layout
heading.pack(pady=10)
task_entry.pack(pady=10)
add_button.pack(pady=5)
task_list.pack(pady=10)
remove_button.pack(pady=5)

# Run the application
root.mainloop()
