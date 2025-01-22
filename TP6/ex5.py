def process_input(user_input):
    try:
        number = int(user_input)
        resultat=10/number
        print(f"le resultat: {resultat}.")
    except ValueError:
        print("Erreur :Nombre invalide")
    except ZeroDivisionError:
        print("Erreur :Division par zero")
        
if __name__=='__main__':
    process_input(input("entrer un nombre:"))