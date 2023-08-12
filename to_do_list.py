import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        list_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = list_tasks.curselection()[0]
        task = list_tasks.get(index)
        confirmed = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the task: '{task}'?")
        if confirmed:
            list_tasks.delete(index)
            tasks.pop(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def main():
    root = tk.Tk()
    root.title("To-Do List")

    global entry_task, list_tasks  # Declare them as global variables

    label_task = tk.Label(root, text="Enter Task:")
    label_task.pack(pady=5)

    entry_task = tk.Entry(root, width=40)
    entry_task.pack(pady=5)

    btn_add = tk.Button(root, text="Add Task", command=add_task)
    btn_add.pack(pady=5)

    btn_delete = tk.Button(root, text="Delete Task", command=delete_task)
    btn_delete.pack(pady=5)

    list_tasks = tk.Listbox(root, width=50)
    list_tasks.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
