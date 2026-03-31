from dataclasses import dataclass, field
from typing import List, Optional, Tuple


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str
    time: str
    frequency: str
    is_complete: bool = False

    def mark_complete(self) -> None:
        pass


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass


class Owner:
    name: str
    pets: List[Pet]

    def __init__(self, name: str, pets: Optional[List[Pet]] = None) -> None:
        pass

    def add_pet(self, pet: Pet) -> None:
        pass

    def get_all_tasks(self) -> List[Task]:
        pass


class Scheduler:
    owner: Owner
    tasks: List[Task]

    def __init__(self, owner: Owner, tasks: Optional[List[Task]] = None) -> None:
        pass

    def get_daily_schedule(self) -> List[Task]:
        pass

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        pass

    def filter_tasks(
        self,
        tasks: List[Task],
        priority: Optional[str] = None,
        frequency: Optional[str] = None,
        is_complete: Optional[bool] = None,
    ) -> List[Task]:
        pass

    def detect_conflicts(self, tasks: List[Task]) -> List[Tuple[Task, Task]]:
        pass
