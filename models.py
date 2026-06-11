class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def complete_task(self):
        self.completed = True

    def to_dict(self):
        return {
            "name": self.name,
            "completed": self.completed
        }

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def to_dict(self):
        return {
            "name": self.name,
            "tasks": [task.to_dict() for task in self.tasks]
        }

class User:
    def __init__(self, username):
        self.username = username
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            "username": self.username,
            "projects": [project.to_dict() for project in self.projects]
        }
