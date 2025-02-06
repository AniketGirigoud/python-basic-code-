x = 80


match x:
    case 0:
        print(0, "print zero")
    case 4:
        print(4, "print four")
    case 5: 
        print(x, "value of x")
    case _ if x!=90:
        print(x, "90 not equal")
    case _ if x!=80:
        print(x, "80 is not ")
    case _:
        print(x)