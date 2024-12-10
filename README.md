                                                                                                                                                                                  ALEJANDRO DÉNIZ SOLANA
                                                                                                                                                                                  
                                                                                                                                                                            
Sistema de Gestión de Tareas con Prioridades



Este repositorio contiene una implementación en Python de un sistema de gestión de tareas basado en prioridades. El programa permite manejar un conjunto de tareas con distintas prioridades, además de gestionar dependencias entre ellas. Incluye persistencia de datos para garantizar que las tareas no se pierdan entre ejecuciones.

Características Principales

1. Añadir Tareas:

• Especifica el nombre, la prioridad (menor número = mayor prioridad) y las dependencias de otras tareas.

• Validación de entradas para evitar datos incompletos o inválidos.

2. Mostrar Tareas Pendientes:

• Lista todas las tareas pendientes, ordenadas por prioridad.

3. Completar Tareas:

• Marca como completada la tarea de mayor prioridad y la elimina del sistema.

4. Obtener la Siguiente Tarea:

• Muestra cuál es la tarea de mayor prioridad sin eliminarla.

5. Verificar Ejecución de Tareas (BONUS):

• Comprueba si una tarea es ejecutable, es decir, si todas sus dependencias han sido completadas.

6. Persistencia de Datos:

• Guarda automáticamente las tareas en un archivo JSON para que se mantengan entre ejecuciones.



Requisitos Técnicos

• Estructura de datos: Se utiliza un heap (cola de prioridad) implementado con el módulo heapq de Python.

• Persistencia: Los datos se almacenan y cargan desde un archivo tasks.json.

• Validación de Entradas: Verifica que el nombre y la prioridad de las tareas sean válidos.

• Ordenamiento por prioridad: Las tareas se gestionan de manera eficiente utilizando la estructura de heap.

