usuarios = []
cuentas = []

def mostrar_menu():
    print("Bienvenido al sistema de caja del banco")
    print("1. Registrar usuario")
    print("2. Depósito")
    print("3. Retiro")
    print("4. Consultar saldo")
    print("5. Salir")

def registrar_usuarios():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        print("El usuario ya esta")
    else:
        usuarios[nombre] = 0.00
        print(f"usuario {nombre} agregado correctamente")


def depositar():
    nombre = input("Introduce el nombre del usuario: ")
    
    if nombre in usuarios:  
        monto = float(input("introduce el monto a depositar: "))
        usuarios[nombre] += monto
    else:
        print(f"Usuario {nombre} no existe")

def retirar():
    nombre = input("Ingrese el nombre del usuario: ")

    if nombre in usuarios: 
       retiro = float(input("Ingrese el monto de retiro: "))
       if retiro > usuarios[nombre]:
           print("Saldo insuficiente para retirar")
       else:
          usuarios[nombre] -= retiro
       
    else:
        print("Usuario no existente en  el sistema")

def consultar_saldo():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        indice = usuarios.index(nombre)
        print(f"Saldo actual: {cuentas[indice]}")
    else:
        print("El usuario no existe.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            registrar_usuarios()
        elif opcion == "2":
            depositar()
        elif opcion == "3":
            retirar()
        elif opcion == "4":
            consultar_saldo()
        elif opcion == "5":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()