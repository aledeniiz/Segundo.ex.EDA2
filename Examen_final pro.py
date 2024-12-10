import heapq
import json
import os

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.heap = []  # Cola de prioridad
        self.filename = filename
        self.load_tasks()

    def add_task(self, name, priority, dependencies=None):
        if not name or not isinstance(priority, int):
            print("Error: El nombre de la tarea y la prioridad son obligatorios y válidos.")
            return
        if dependencies is None:
            dependencies = []
        task = {"name": name, "priority": priority, "dependencies": dependencies}
        heapq.heappush(self.heap, (priority, task))
        print(f"Tarea '{name}' añadida con prioridad {priority} y dependencias {dependencies}.")
        self.save_tasks()

    def show_tasks(self):
        if not self.heap:
            print("No hay tareas pendientes.")
            return
        print("Tareas pendientes en orden de prioridad:")
        for _, task in sorted(self.heap):
            print(f"Tarea: {task['name']}, Prioridad: {task['priority']}, Dependencias: {task['dependencies']}")

    def complete_task(self):
        if not self.heap:
            print("No hay tareas para completar.")
            return
        _, task = heapq.heappop(self.heap)
        print(f"Tarea completada: {task['name']}")
        self.save_tasks()

    def get_next_task(self):
        if not self.heap:
            print("No hay tareas disponibles.")
            return
        priority, task = self.heap[0]
        print(f"Siguiente tarea de mayor prioridad: {task['name']}, Prioridad: {priority}")

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.heap, f)
        print("Tareas guardadas exitosamente.")

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.heap = json.load(f)
            heapq.heapify(self.heap)
            print("Tareas cargadas exitosamente.")
        else:
            print("No se encontró un archivo de tareas previo. Iniciando un nuevo gestor de tareas.")

    def is_task_executable(self, name):
        task = next((t for _, t in self.heap if t["name"] == name), None)
        if not task:
            print(f"Tarea '{name}' no encontrada.")
            return
        dependencies_completed = all(dep not in [t["name"] for _, t in self.heap] for dep in task["dependencies"])
        if dependencies_completed:
            print(f"La tarea '{name}' es ejecutable.")
        else:
            print(f"La tarea '{name}' no es ejecutable porque tiene dependencias pendientes.")

# Interfaz de usuario
if __name__ == "__main__":
    manager = TaskManager()

    while True:
        print("\n--- Menú de Gestión de Tareas ---")
        print("1. Añadir nueva tarea")
        print("2. Mostrar tareas pendientes")
        print("3. Marcar tarea como completada")
        print("4. Obtener la siguiente tarea de mayor prioridad")
        print("5. Verificar si una tarea es ejecutable")
        print("6. Salir")

        option = input("Selecciona una opción: ")

        if option == "1":
            name = input("Nombre de la tarea: ")
            priority = int(input("Prioridad (número entero, menor es mayor prioridad): "))
            dependencies = input("Dependencias (separadas por coma, deja vacío si no hay): ").split(",")
            dependencies = [d.strip() for d in dependencies if d.strip()]
            manager.add_task(name, priority, dependencies)
        elif option == "2":
            manager.show_tasks()
        elif option == "3":
            manager.complete_task()
        elif option == "4":
            manager.get_next_task()
        elif option == "5":
            name = input("Nombre de la tarea para verificar: ")
            manager.is_task_executable(name)
        elif option == "6":
            print("Saliendo del gestor de tareas. ¡Adiós!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
