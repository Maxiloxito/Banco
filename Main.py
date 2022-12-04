from User import User

def main():

    client_x = 0
    name = ""
    run = 0 
    account_number = 0
    amount = 0

    name = input("Ingrese el nombre del cliente: ")
    run = int(input("Ingrese el rut del cliente: "))
    account_number = int(input("Ingrese el numero de cuenta del cliente: "))
    

    client_x = User(name,run,account_number,amount)
    print("Usuario creado\n")
    client_x.show()
    print("\n")
    print("Desea ingresar un monto?")
    print("1.-Si    y    2.-No")
    print("Ingrese el numero de la opcion")
    opcion = int(input())
    if(opcion == 1):
        client_x.withdraw()
        print("\n")
        client_x.show()
    else:
        print("Gracias!")

    

if __name__ == "__main__":
    main()
