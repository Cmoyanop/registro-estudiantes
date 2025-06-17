## Código Python `sistema_estudiantes.py` comentado

# sistema_estudiantes.py

# Lista global para almacenar los estudiantes registrados
estudiantes = []

def registrar_estudiante():
    """
    Función para registrar un nuevo estudiante.
    Solicita el nombre y la nota, valida la nota,
    y agrega el estudiante a la lista.
    """
    nombre = input("Ingrese el nombre del estudiante: ")  # Solicitar nombre al usuario
    try:
        nota = float(input("Ingrese la nota del estudiante: "))  # Solicitar nota y convertir a float
        if 0 <= nota <= 10:  # Validar que la nota esté dentro del rango permitido
            estudiantes.append({"nombre": nombre, "nota": nota})  # Agregar estudiante a la lista
            print("✅ Estudiante registrado correctamente.")
        else:
            print("⚠️ La nota debe estar entre 0 y 10.")  # Mensaje si la nota no es válida
    except ValueError:
        print("⚠️ Entrada inválida. Ingrese un número válido.")  # Captura error si la nota no es numérica

def mostrar_estudiantes():
    """
    Función para mostrar la lista de estudiantes registrados.
    """
    if not estudiantes:  # Verifica si la lista está vacía
        print("📭 No hay estudiantes registrados.")
    else:
        for idx, est in enumerate(estudiantes):  # Itera con índice para numerar la lista
            print(f"{idx+1}. {est['nombre']} - Nota: {est['nota']}")  # Imprime nombre y nota

def calcular_promedio():
    """
    Función para calcular y mostrar el promedio general de las notas.
    """
    if not estudiantes:  # Verifica que existan estudiantes para calcular promedio
        print("❌ No hay datos para calcular promedio.")
    else:
        total = sum(est["nota"] for est in estudiantes)  # Suma todas las notas
        promedio = total / len(estudiantes)  # Calcula promedio dividiendo por número de estudiantes
        print(f"📊 Promedio general: {promedio:.2f}")  # Muestra promedio con 2 decimales

def menu():
    """
    Menú principal del sistema.
    Permite al usuario elegir qué acción realizar.
    """
    while True:
        print("\n--- SISTEMA DE REGISTRO DE ESTUDIANTES ---")
        print("1. Registrar Estudiante")
        print("2. Mostrar Lista")
        print("3. Calcular Promedio")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")  # Solicita opción al usuario
        
        if opcion == '1':
            registrar_estudiante()  # Llama función para registrar estudiante
        elif opcion == '2':
            mostrar_estudiantes()  # Llama función para mostrar estudiantes
        elif opcion == '3':
            calcular_promedio()  # Llama función para calcular promedio
        elif opcion == '4':
            print("👋 Saliendo del sistema. ¡Hasta pronto!")  # Mensaje de salida
            break  # Termina el ciclo y sale del programa
        else:
            print("⚠️ Opción no válida. Intente de nuevo.")  # Mensaje para opción incorrecta

# Ejecuta el programa llamando al menú principal
if __name__ == "__main__":
    menu()
