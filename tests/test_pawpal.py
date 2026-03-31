from pawpal_system import Task, Pet


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