import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = self.load_tasks()

        self.task_id = tk.IntVar()
        self.task_title = tk.StringVar()
        self.task_description = tk.StringVar()
        self.task_completed = tk.BooleanVar()

        self.create_widgets()

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = []
                for line in file:
                    task_id, title, description, completed = line.strip().split(",")
                    tasks.append({
                        "id": int(task_id),
                        "title": title,
                        "description": description,
                        "completed": completed == "True"
                    })
                return tasks
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task['id']},{task['title']},{task['description']},{task['completed']}\n")

    def add_task(self):
        title = self.task_title.get()
        description = self.task_description.get()
        task_id = len(self.tasks) + 1
        self.tasks.append({
            "id": task_id,
            "title": title,
            "description": description,
            "completed": False
        })
        self.save_tasks()
        self.task_listbox.insert(tk.END, f"Task {task_id}: {title} - {description} - Not completed")
        self.task_title.set("")
        self.task_description.set("")

    def list_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Completed" if task["completed"] else "Not completed"
            self.task_listbox.insert(tk.END, f"Task {task['id']}: {task['title']} - {task['description']} - {status}")

    def mark_task_as_completed(self):
        task_id = int(self.task_id.get())
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                self.list_tasks()
                return
        messagebox.showerror("Error", "Task not found")

    def delete_task(self):
        task_id = int(self.task_id.get())
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                self.list_tasks()
                return
        messagebox.showerror("Error", "Task not found")

    def create_widgets(self):
        # Task title and description entry fields
        tk.Label(self.root, text="Task Title:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.task_title).grid(row=0, column=1)
        tk.Label(self.root, text="Task Description:").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.task_description).grid(row=1, column=1)

        # Add task button
        tk.Button(self.root, text="Add Task", command=self.add_task).grid(row=2, column=0, columnspan=2)

        # Task listbox
        tk.Label(self.root, text="Task List:").grid(row=3, column=0)
        self.task_listbox = tk.Listbox(self.root, width=40)
        self.task_listbox.grid(row=4, column=0, columnspan=2)

        # Mark task as completed and delete task fields
        tk.Label(self.root, text="Task ID:").grid(row=5, column=0)
        tk.Entry(self.root, textvariable=self.task_id).grid(row=5, column=1)
        tk.Button(self.root, text="Mark as Completed", command=self.mark_task_as_completed).grid(row=6, column=0)
        tk.Button(self.root, text="Delete Task", command=self.delete_task).grid(row=6, column=1)

        # List tasks button
        tk.Button(self.root, text="List Tasks", command=self.list_tasks).grid(row=7, column=0, columnspan=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
