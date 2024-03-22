def change():
    expense = 23.75
    money = 100
    print ("Ingresar gasto:")
    print (expense)
    print ("Dinero recibido")
    print (money)
    print ("\nVuelto")
    print ("\nPesos:")
    resta = int (money - expense)
    print (resta)
    print ("Centavos:")
    cent = (money - expense)
    print (int ((cent - resta) * 100))
