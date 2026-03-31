from pawpal_system import Task, Pet, Owner, Scheduler


def test_add_task():
    pet = Pet("Mochi", "dog")
    task = Task("Walk", 20, "high", "09:00")

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0].title == "Walk"


def test_mark_complete():
    task = Task("Feed", 10, "high", "08:00")

    task.mark_complete()

    assert task.completed is True


def test_sort_by_time():
    scheduler = Scheduler()
    tasks = [
        Task("Play", 15, "medium", "10:00"),
        Task("Feed", 10, "high", "08:00"),
        Task("Walk", 20, "high", "09:00"),
    ]

    sorted_tasks = scheduler.sort_by_time(tasks)

    assert sorted_tasks[0].title == "Feed"
    assert sorted_tasks[1].title == "Walk"
    assert sorted_tasks[2].title == "Play"


def test_detect_conflicts():
    scheduler = Scheduler()
    tasks = [
        Task("Feed", 10, "high", "08:00"),
        Task("Medicine", 5, "high", "08:00"),
        Task("Walk", 20, "medium", "09:00"),
    ]

    conflicts = scheduler.detect_conflicts(tasks)

    assert len(conflicts) == 1
    assert "Medicine" in conflicts[0]


def test_daily_recurring_task_creates_new_task():
    scheduler = Scheduler()
    pet = Pet("Mochi", "dog")
    task = Task("Feed breakfast", 10, "high", "08:00", frequency="daily")

    pet.add_task(task)
    scheduler.mark_task_complete(pet, task)

    assert pet.tasks[0].completed is True
    assert len(pet.tasks) == 2
    assert pet.tasks[1].title == "Feed breakfast"
    assert pet.tasks[1].completed is False
    assert pet.tasks[1].frequency == "daily"


def test_filter_completed_tasks():
    scheduler = Scheduler()
    tasks = [
        Task("Feed", 10, "high", "08:00", completed=True),
        Task("Walk", 20, "medium", "09:00", completed=False),
    ]

    completed_tasks = scheduler.filter_tasks(tasks, completed=True)
    incomplete_tasks = scheduler.filter_tasks(tasks, completed=False)

    assert len(completed_tasks) == 1
    assert completed_tasks[0].title == "Feed"

    assert len(incomplete_tasks) == 1
    assert incomplete_tasks[0].title == "Walk"