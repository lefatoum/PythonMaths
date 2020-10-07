def nbre_solutions(a, b, c):
    if a == 0:
        print("Léquation est du premier degré")
    else:
        delta = b**2 - 4*a*c
        if delta > 0:
            print("L'équation possède deux solutions réelles.")
        else:
            if delta ==0:
                print("L'équation possède une solution réelle")
            else:
                print("L'équation ne possède pas de solution réelle")