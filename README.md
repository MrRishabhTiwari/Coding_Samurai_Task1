# To-Do List Application

This application allows users to manage tasks effectively through a graphical user interface (GUI) built using Tkinter in Python.

## Features

- **Add Tasks**: Users can add new tasks by entering a title and description. Tasks are automatically assigned an ID and marked as not completed initially.
  
- **List Tasks**: Displays all existing tasks with their details (ID, title, description, and completion status).

- **Mark as Completed**: Allows users to mark a task as completed by specifying its ID.

- **Delete Task**: Enables users to delete a task by specifying its ID.

- **Data Persistence**: Tasks are stored in a text file (`tasks.txt`) and are loaded into the application upon startup.

## Installation
Install dependencies (Python 3 and tkinter are required):
   ```
   pip install tk
   ```

## Usage

Run the application using Python

### Adding a Task

1. Enter a task title and description in the respective entry fields.
2. Click on the "Add Task" button to add the task.

### Listing Tasks

Click on the "List Tasks" button to display all current tasks in the listbox.

### Marking a Task as Completed

1. Enter the ID of the task you want to mark as completed in the "Task ID" entry field.
2. Click on the "Mark as Completed" button.

### Deleting a Task

1. Enter the ID of the task you want to delete in the "Task ID" entry field.
2. Click on the "Delete Task" button.

## Data Storage

Task information is stored in the `tasks.txt` file in the following format:
```
id,title,description,completed
```

- `id`: Unique identifier for each task.
- `title`: Title of the task.
- `description`: Description of the task.
- `completed`: Boolean value (`True` or `False`) indicating whether the task is completed or not.
