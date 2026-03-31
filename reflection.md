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

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
