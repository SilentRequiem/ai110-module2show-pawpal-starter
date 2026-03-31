from pawpal_system import Owner, Pet, Task, Scheduler


owner = Owner("Michael")

pet1 = Pet("Mochi", "dog")
pet2 = Pet("Luna", "cat")

task1 = Task("Morning walk", 20, "high", "09:00")
task2 = Task("Feed breakfast", 10, "high", "08:00")
task3 = Task("Play time", 15, "medium", "10:00")

pet1.add_task(task1)
pet1.add_task(task2)
pet2.add_task(task3)

owner.add_pet(pet1)
owner.add_pet(pet2)

scheduler = Scheduler()
schedule = scheduler.get_daily_schedule(owner)

print("Today's Schedule")
print("-----------------")
for task in schedule:
    print(f"{task.time} - {task.title} ({task.priority}, {task.duration_minutes} mins)")