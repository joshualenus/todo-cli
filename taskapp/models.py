from datetime import datetime
from dataclasses import dataclass, asdict, field


@dataclass()
class Task:
    task: str
    completed: bool = False
    time_made: str = field(default_factory=lambda: datetime.now().isoformat()) #must use default factory else datetime will remain as time when first created

    #should store in isoformat so can compare more easily, but create a function so can display more readable text
    def get_display_time(self):
        dt = datetime.fromisoformat(self.time_made)
        return dt.strftime("%b %d, %I:%M %p") 
    
    def to_dict (self):
        return asdict(self)
    
    @staticmethod
    def from_dict (tasks: dict):
        return Task(**tasks)