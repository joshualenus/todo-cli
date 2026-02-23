import pytest
from pathlib import Path
from taskapp.manager import TaskManager
from taskapp.models import Task

@pytest.fixture
def taskmanager (tmp_path):
    path = tmp_path / 'testing.json'
    return TaskManager(str(path))

def test_add (taskmanager):
    task = Task("Buy Milk")
    taskmanager.add(task)
    tasks = taskmanager.load_tasks()
    assert len(tasks) == 1
    assert tasks[0].task == "Buy Milk"
    assert tasks[0].completed == False

def test_add_multiple(taskmanager):
    task1 = Task("Buy Milk")
    task2 = Task("Buy Eggs")
    taskmanager.add(task1)
    taskmanager.add(task2)
    tasks = taskmanager.load_tasks()
    assert len(tasks) == 2


def test_completed(taskmanager):
    task = Task("Buy Milk")
    taskmanager.add(task)
    taskmanager.completed(1)
    tasks = taskmanager.load_tasks()
    assert tasks[0].completed == True

def test_completed_invalidnumber(taskmanager):
    task = Task("Buy Milk")
    taskmanager.add(task)
    taskmanager.completed(99)
    tasks = taskmanager.load_tasks()
    assert tasks[0].completed == False
    
def test_delete(taskmanager):
    task = Task("Buy Milk")
    taskmanager.add(task)
    taskmanager.delete(1)
    tasks = taskmanager.load_tasks()
    assert len(tasks) == 0

def test_deleted_invalidnumber(taskmanager):
    task = Task("Buy Milk")
    taskmanager.add(task)
    taskmanager.delete(99)
    tasks = taskmanager.load_tasks()
    assert len(tasks) == 1

def test_persistence(tmp_path):
    path = tmp_path / "testing.json"
    manager1 = TaskManager(str(path))
    manager1.add(Task("Buy Milk"))

    manager2 = TaskManager(str(path))
    tasks = manager2.load_tasks()
    assert len(tasks) == 1
    assert tasks[0].task == "Buy Milk"



