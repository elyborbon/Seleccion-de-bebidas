class Bebida:
    def __init__(self, costo1, costo2, costo3, costo4):
        self.costo1 = costo1
        self.costo2= costo2
        self.costo3 = costo3
        self.costo4 = costo4
       

    def seleccion (self):
        print("BEBIDA")
        print ("Boton 1. Coca Cola, $", self.costo1)
        print ("Boton 2. Sprite, $", self.costo2)
        print ("Boton 3. Lift, $", self.costo3)
        print ("Boton 4. Fresca, $", self.costo4)

    def elegir (self):
        bebidas = int (input ("Selecciona tu bebida:  "))
        if bebidas == 1:
            print ("Selecciono Coca Cola ")

        elif bebidas == 2:
            print ("Selecciono Sprite")
        elif bebidas == 3:
            print ("Selecciono Lift")
        else:
            print ("Selecciono Fresca")

    def hielos (self, hiel):
        self.hiel = hiel
        if  hiel == "yes":
            print ("Bebida con hielo")
        else:
            print ("Bebida sin hielo")

    def metodo (self, metodos):
        self.metodos = metodos 
     #   print ("Pulse 1. Tarjeta de credito")
     #   print("Pulse 2. Efectivo")
        if self.metodos == "Efectivo":
            print("Pagado con Efectivo")
        elif self.metodos == "Tarjeta de credito":
            print("Pagado con Tarjeta de credito")
        else:
            print("Exit")

bebida1 = Bebida(20, 18, 15, 12)    
bebida1.seleccion()
bebida1.elegir()
bebida1.hielos("No")
bebida1.metodo("Efectivo")

bebida2 =Bebida(18, 19, 20, 21)
bebida2.seleccion()
bebida2.elegir()
bebida2.hielos("yes")
bebida2.metodo("Tarjeta de credito")