import json
from pathlib import Path
from rich.console import Console
from rich.table import Table

from .models import Task

console = Console()

class TaskManager:
    def __init__ (self, filepath: str):
        self.filepath = Path(filepath)
        if not self.filepath.exists():
            self.filepath.write_text("[]")

    def load_tasks (self):
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)
                return [Task.from_dict(task) for task in data]
        except json.JSONDecodeError:
            raise ValueError("File is corrupted")
    
    def save_tasks (self, tasks:list[Task]):
        converted = [task.to_dict() for task in tasks]
        with open(self.filepath, 'w') as f:
            json.dump(converted, f, indent = 2)
    
    def add(self, task_new: Task):
        try:
            tasks_existing = self.load_tasks()
        except ValueError as e:
            console.print(f"[red]{e}[/red]")
            return 
        
        tasks_existing.append(task_new)
        console.print(f"{task_new.task} successfully added")
        self.save_tasks(tasks_existing)

    def completed(self, number: int):
        try:
            tasks_existing = self.load_tasks()
        except ValueError as e:
            console.print(f"[red]{e}[/red]")
            return 
        for i, task in enumerate(tasks_existing, start=1):
            if i == number:
                task.completed = True
                console.print(f"Updated {task.task} as completed")
                self.save_tasks(tasks_existing)
                return 
        console.print("Task not found")

    def view(self):
        try:
            tasks = self.load_tasks()
        except ValueError as e:
            console.print(f"[red]{e}[/red]")
            return 
        if not tasks:
            console.print("[yellow]No tasks yet! Add one with:[/yellow] [cyan]add 'Your task'[/cyan]")
            return
        table = Table(title="To do list")
        table.add_column("#", style="white", justify="right")
        table.add_column("Task", style="white")
        table.add_column("Status", justify="center")
        table.add_column("Time made", style="white")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task.completed else "⬜"
            table.add_row(str(i), task.task, status, task.get_display_time())
        console.print(table)
    
    def delete(self, number:int):
        try:
            tasks = self.load_tasks()
        except ValueError as e:
            console.print(f"[red]{e}[/red]")
            return 
        
        for i, task in enumerate(tasks, start=1):
            if i == number:
                console.print(f"Deleted task: {task.task}")
                tasks.pop(i)
                self.save_tasks(tasks)
                return
        console.print("Task not found")