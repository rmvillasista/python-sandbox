import json
import sys
from pathlib import Path

DB_FILE = Path("hero_db.json")

def load_db():
    try:
        if DB_FILE.exists():
            with open(DB_FILE, "r") as f:
                return json.load(f)
    except json.JSONDecodeError:
        print("Warning: Database corrupt. Starting fresh.")
    return []

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

def main():
    tasks = load_db()
    if len(sys.argv) < 2:
        print("Usage: python hero_app.py [add <title> | list | done <id>]")
        return

    command = sys.argv[1].lower()

    if command == "add" and len(sys.argv) > 2:
        title = " ".join(sys.argv[2:])
        new_id = max([t["id"] for t in tasks], default=0) + 1
        tasks.append({"id": new_id, "title": title, "done": False})
        save_db(tasks)
        print(f"Added task #{new_id}")

    elif command == "list":
        for t in tasks:
            status = "x" if t["done"] else " "
            print(f"[{status}] {t['id']}: {t['title']}")

    elif command == "done" and len(sys.argv) > 2:
        try:
            target_id = int(sys.argv[2])
            for t in tasks:
                if t["id"] == target_id:
                    t["done"] = True
                    save_db(tasks)
                    print(f"Task #{target_id} marked complete.")
                    return
            print(f"Task #{target_id} not found.")
        except ValueError:
            print("Error: Task ID must be an integer.")

if __name__ == "__main__":
    main()