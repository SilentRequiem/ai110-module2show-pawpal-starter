# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

The design I have created includes four classes: Owner, Pet, Task, and Scheduler. The Owner class includes the name of the owner and their pets. The Pet class includes the name, species, and task of the pets. The Task class represents a task such as feeding, walking, or giving medication to a pet. It includes information such as task duration, priority, time, frequency, and if it is done or not. The Scheduler class includes logic such as collecting, sorting, and filtering tasks, and checking for conflicts. I have chosen these classes because they match the system.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Right now, I've kept the design simple and haven't made any major changes. I might change how the Scheduler gets its tasks from the Owner to ensure the roles remain clear. For now, I've concentrated on making the design simple to construct and understand.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

My scheduler considers time, completion status, and task frequency. Time is used to sort tasks so they are in the correct order. Completion status is used for filtering tasks so the user can view completed or incomplete tasks. Frequency is used to handle recurring tasks like daily or weekly tasks. I decided these constraints mattered most because they directly affect how a user plans their day and keeps track of important tasks.

**b. Tradeoffs**

One tradeoff my scheduler makes is that it only checks for exact time conflicts instead of overlapping durations. This means two tasks with different durations but overlapping times will not be detected as a conflict. This tradeoff is reasonable because it keeps the logic simple and still solves the main problem for this project.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI to help design my system, generate class skeletons, and debug issues. I also used it to help connect my backend logic to the Streamlit UI and to create test cases. The most helpful prompts were ones where I clearly described what I wanted, like generating a class structure or fixing a specific error.

**b. Judgment and verification**

There were times where I did not accept AI suggestions directly. For example, when adding new features, I made sure the logic matched my design and did not overcomplicate the system. I verified suggestions by running my code, checking outputs, and using tests to make sure everything worked correctly.

---

## 4. Testing and Verification

**a. What you tested**

I tested adding tasks, marking tasks complete, sorting tasks by time, detecting conflicts, filtering tasks, and recurring task creation. These tests were important because they verify the main features of the scheduler and ensure the system behaves as expected.

**b. Confidence**

I am confident that my scheduler works correctly because all of my tests passed. The main features like sorting, filtering, and recurrence are working. If I had more time, I would test edge cases such as duplicate task names, invalid time inputs, and more complex scheduling scenarios.

---

## 5. Reflection

**a. What went well**

The part that went well was building the system step by step. Starting with the design and then implementing each part made the project easier to manage. The connection between the backend and the UI also worked well.

**b. What you would improve**

If I had another iteration, I would improve the UI and make it more user friendly. I would also improve the conflict detection to handle overlapping time ranges instead of just exact matches.

**c. Key takeaway**

One important thing I learned is that designing the system first makes coding much easier. Working with AI was helpful, but I still needed to understand the logic and make sure everything worked correctly.