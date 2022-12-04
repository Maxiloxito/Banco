class User:

    def __init__(self,name,run,account_number=0,amount=0):
        self.name = name
        self.run = run
        self.account_number = account_number
        self.amount = amount

    def withdraw(self):
        print("Ingresar dinero")
        print("Saldo: ",self.amount)
        amount = int(input("Ingrese el monto a depositar: "))
        if(amount>0):
            self.amount += amount

    def show(self):
        print("Nombre: ",self.name)
        print("Run: ",self.run)
        print("Numero de cuenta: ",self.account_number)
        print("Saldo: ",self.amount)

        
