import json
from pathlib import Path

DATA_FILE = Path("tasks.json")

def save_tasks(tasks_list):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks_list, f, indent=2)

def load_tasks():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Execution
sample_data = [{"id": 101, "title": "Setup CI/CD"}, {"id": 102, "title": "Write unit tests"}]
save_tasks(sample_data)

loaded = load_tasks()
print(f"Successfully loaded {len(loaded)} tasks from {DATA_FILE.name}")