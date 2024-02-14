import tkinter as tk
from tkinter import simpledialog, messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=40, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        update_button = tk.Button(root, text="Update Task", command=self.update_task)
        update_button.grid(row=2, column=0, padx=10, pady=10)

        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.grid(row=2, column=1, padx=10, pady=10)

        self.load_tasks()

        root.protocol("WM_DELETE_WINDOW", self.on_close)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.save_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            new_task = simpledialog.askstring("Input", "Update Task:", parent=self.root)
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, new_task)
                self.save_tasks()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            task_to_delete = self.tasks[selected_task_index]
            confirm = messagebox.askyesno("Confirm Deletion", f"Do you want to delete task: {task_to_delete}?")
            if confirm:
                self.task_listbox.delete(selected_task_index)
                del self.tasks[selected_task_index]
                self.save_tasks()

    def load_tasks(self):
        try:
            with open("tasks_gui.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
            for task in self.tasks:
                self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks_gui.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def on_close(self):
        self.save_tasks()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

