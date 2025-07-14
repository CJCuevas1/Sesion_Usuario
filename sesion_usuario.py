# Este programa demuestra el uso de constructores y destructores en Python y
# simula una sesión de usuario interactiva con un menú de opciones.

import datetime
import time

# Esta clase presenta la lógica para la sesión de un usuario.
class SesionUsuario:
    
    # Este es el método constructor, se ejecuta al iniciar la sesión.
    def __init__(self, nombre_usuario):
        # Esta variable almacena el nombre del usuario que inicia sesión.
        self.nombre_usuario = nombre_usuario
        # Esta variable almacena la hora exacta de la conexión.
        self.hora_inicio = datetime.datetime.now()
        
        print(f"\n✅ CONSTRUCTOR: ¡Bienvenido, '{self.nombre_usuario}'! Sesión iniciada.")
        print(f"   -> Hora de conexión: {self.hora_inicio.strftime('%H:%M:%S')}")

    # Esta función presenta los detalles del perfil del usuario.
    def ver_perfil(self):
        print("\n--- Perfil de Usuario ---")
        print(f"  Nombre: {self.nombre_usuario}")
        print(f"  Sesión iniciada a las: {self.hora_inicio.strftime('%H:%M:%S')}")
        print("------------------------")

    # Esta función simula una tarea que realiza el usuario.
    def realizar_accion(self):
        print(f"\n   -> ACCIÓN: '{self.nombre_usuario}' está trabajando en el sistema...")
        # Esta línea aplica una pausa para simular el tiempo de trabajo.
        time.sleep(1)
        print("   -> ¡Tarea completada!")

    # Este es el método destructor, se ejecuta al cerrar la sesión.
    def __del__(self):
        print(f"\n❌ DESTRUCTOR: Adiós, '{self.nombre_usuario}'. Sesión cerrada.")
        print(f"   -> La sesión ha terminado de forma segura.")


# En este bloque inicia el programa.


print("--- Inicio del sistema de autenticación ---")

# El sistema solicita el nombre de usuario para iniciar.
nombre_ingresado = input("Por favor, introduce tu nombre de usuario: ")

# Esta línea invoca la clase para crear el objeto de la sesión.
sesion_activa = SesionUsuario(nombre_ingresado)

# Este bucle mantiene el menú de opciones activo hasta que se elija salir.
while True:
    print("\n-- MENÚ DE OPCIONES --")
    print("1. Realizar una acción de trabajo")
    print("2. Ver mi perfil")
    print("3. Cerrar sesión")
    
    # Esta variable almacena la opción seleccionada por el usuario.
    opcion = input("Elige una opción (1, 2 o 3): ")

    # En caso de que el usuario elija la opción '1', se ejecuta este bloque.
    if opcion == '1':
        sesion_activa.realizar_accion()
    
    # En caso de que el usuario elija la opción '2', se ejecuta este bloque.
    elif opcion == '2':
        sesion_activa.ver_perfil()
    
    # En caso de que el usuario elija la opción '3', se ejecuta este.
    elif opcion == '3':
        print("\nCerrando sesión...")
        # Esta línea finaliza el bucle para terminar el programa.
        break
    
    # Este bloque gestiona las entradas no válidas.
    else:
        print("\nOpción no válida. Por favor, elige 1, 2 o 3.")

# Se presenta un mensaje final al terminar el programa.
print("\n--- Fin del sistema ---")