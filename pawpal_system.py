from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str
    time: str
    frequency: str = "once"
    completed: bool = False
    due_date: date = field(default_factory=date.today)

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        """Add a task to this pet."""
        self.tasks.append(task)

    def remove_task(self, task):
        """Remove a task from this pet if it exists."""
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self):
        """Return all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    name: str
    pets: list = field(default_factory=list)

    def add_pet(self, pet):
        """Add a pet to this owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return all tasks from all pets owned by this owner."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    def get_daily_schedule(self, owner):
        """Get a daily schedule for the owner's tasks."""
        tasks = owner.get_all_tasks()
        return self.sort_by_time(tasks)

    def sort_by_time(self, tasks):
        """Sort tasks by time in ascending order."""
        return sorted(tasks, key=lambda task: task.time)

    def filter_tasks(self, tasks, completed=None, pet_name=None):
        """Filter tasks by completion status."""
        filtered_tasks = tasks

        if completed is not None:
            filtered_tasks = [task for task in filtered_tasks if task.completed == completed]

        return filtered_tasks

    def detect_conflicts(self, tasks):
        """Detect tasks that share the same time."""
        conflicts = []
        seen_times = {}

        for task in tasks:
            if task.time in seen_times:
                conflicts.append(f"Conflict: {task.title} has the same time as {seen_times[task.time]}")
            else:
                seen_times[task.time] = task.title

        return conflicts

    def mark_task_complete(self, pet, task):
        """Mark a task complete and recreate it if it is recurring."""
        task.mark_complete()

        if task.frequency == "daily":
            new_task = Task(
                title=task.title,
                duration_minutes=task.duration_minutes,
                priority=task.priority,
                time=task.time,
                frequency=task.frequency,
                due_date=task.due_date + timedelta(days=1)
            )
            pet.add_task(new_task)

        elif task.frequency == "weekly":
            new_task = Task(
                title=task.title,
                duration_minutes=task.duration_minutes,
                priority=task.priority,
                time=task.time,
                frequency=task.frequency,
                due_date=task.due_date + timedelta(days=7)
            )
            pet.add_task(new_task)