# Dictionary of task objects
tasks = [
    {"id": 1, "title": "Buy groceries", "completed": False, "tags": {"home", "errand"}},
    {"id": 2, "title": "Read Python docs", "completed": True, "tags": {"learning", "tech"}},
    {"id": 3, "title": "Clean desk", "completed": False, "tags": {"home"}},
]

# Collect all unique tags using Set operations
all_tags = set()
for task in tasks:
    all_tags.update(task["tags"])

print("All unique tags:", all_tags)

# Filter pending tasks using List Comprehension
pending = [t["title"] for t in tasks if not t["completed"]]
print("Pending tasks:", pending)