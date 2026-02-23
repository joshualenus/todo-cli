import typer 
from .models import Task
from .manager import TaskManager

app = typer.Typer()
taskmanager = TaskManager("todolist.json")

@app.command()
def add(task:str):
    new_task = Task(task)
    taskmanager.add(new_task)

@app.command()
def completed (number : int):
    taskmanager.completed(number)

@app.command()
def view():
    taskmanager.view()

@app.command()
def delete(number:int):
    taskmanager.delete(number)

if __name__ == '__main__':
    app()