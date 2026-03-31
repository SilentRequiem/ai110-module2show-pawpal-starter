import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if "owner" not in st.session_state:
    st.session_state.owner = Owner(owner_name)

if "pet" not in st.session_state:
    st.session_state.pet = Pet(pet_name, species)

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.session_state.owner.name = owner_name
st.session_state.pet.name = pet_name
st.session_state.pet.species = species

if st.session_state.pet not in st.session_state.owner.pets:
    st.session_state.owner.add_pet(st.session_state.pet)

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
with col4:
    task_time = st.text_input("Time (HH:MM)", value="09:00")
with col5:
    frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])

if st.button("Add task"):
    new_task = Task(
        title=task_title,
        duration_minutes=int(duration),
        priority=priority,
        time=task_time,
        frequency=frequency
    )

    st.session_state.pet.add_task(new_task)

    st.session_state.tasks.append(
        {
            "title": new_task.title,
            "duration_minutes": new_task.duration_minutes,
            "priority": new_task.priority,
            "time": new_task.time,
            "frequency": new_task.frequency,
            "completed": new_task.completed
        }
    )

    st.success(f"Added task: {new_task.title}")

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)

    st.markdown("### Mark Task Complete")
    task_options = [task.title for task in st.session_state.pet.get_tasks()]
    selected_task = st.selectbox("Select a task to complete", task_options)

    if st.button("Mark complete"):
        for task in st.session_state.pet.get_tasks():
            if task.title == selected_task and not task.completed:
                st.session_state.scheduler.mark_task_complete(st.session_state.pet, task)
                break

        updated_tasks = []
        for task in st.session_state.pet.get_tasks():
            updated_tasks.append(
                {
                    "title": task.title,
                    "duration_minutes": task.duration_minutes,
                    "priority": task.priority,
                    "time": task.time,
                    "frequency": task.frequency,
                    "completed": task.completed
                }
            )

        st.session_state.tasks = updated_tasks
        st.success(f"Marked '{selected_task}' as complete.")
else:
    st.info("No tasks yet. Add one above.")

st.divider()

status_filter = st.selectbox(
    "Filter tasks",
    ["all", "completed", "incomplete"]
)

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    tasks = st.session_state.pet.get_tasks()

    if not tasks:
        st.warning("No tasks to schedule.")
    else:
        scheduler = st.session_state.scheduler

        if status_filter == "completed":
            tasks = scheduler.filter_tasks(tasks, completed=True)
        elif status_filter == "incomplete":
            tasks = scheduler.filter_tasks(tasks, completed=False)

        if not tasks:
            st.warning("No tasks match that filter.")
        else:
            sorted_tasks = scheduler.sort_by_time(tasks)
            conflicts = scheduler.detect_conflicts(sorted_tasks)

            st.success("Schedule generated!")

            st.subheader("Today's Schedule")
            for task in sorted_tasks:
                st.write(
                    f"{task.time} - {task.title} "
                    f"({task.priority}, {task.duration_minutes} mins, {task.frequency})"
                )

            if conflicts:
                st.subheader("Conflicts")
                for conflict in conflicts:
                    st.warning(conflict)