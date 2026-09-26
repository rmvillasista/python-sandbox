from base_task import BaseTask
from tasks import StandardTask, TimedTask


def main():
    tasks: list[BaseTask] = [
        StandardTask(1, "Master Python OOP"),
        TimedTask(2, "Build OOP Architecture Demo", 45),
    ]

    for task in tasks:
        print("Before:", task)
        task.mark_complete()
        print("After: ", task)
        print("Dict Export:", task.to_dict())
        print("-" * 40)


if __name__ == "__main__":
    main()