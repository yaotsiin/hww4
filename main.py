
class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def show_task(self):
        status = "Виконано" if self.completed else "Не виконано"
        print(f"Назва: {self.title}")
        print(f"Опис: {self.description}")
        print(f"Дедлайн: {self.deadline}")
        print(f"Стан: {status}")
        print("-" * 30)


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Завдання успішно додано!")

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print("Завдання успішно видалено!")
                return
        print("Завдання не знайдено.")

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                print("Завдання позначено як виконане!")
                return
        print("Завдання не знайдено.")

    def show_tasks(self):
        if not self.tasks:
            print("Список завдань порожній.")
            return

        for task in self.tasks:
            task.show_task()


manager = TaskManager()

task1 = Task(
    "Вивчити Python",
    "Повторити класи та об'єкти",
    "05.11.2026"
)

task2 = Task(
    "Виконати домашнє завдання",
    "Написати програму на Python",
    "07.11.2026"
)

manager.add_task(task1)
manager.add_task(task2)

print("\nСписок завдань:")
manager.show_tasks()

manager.complete_task("Вивчити Python")

manager.delete_task("Виконати домашнє завдання")

print("\nОновлений список завдань:")
manager.show_tasks()
