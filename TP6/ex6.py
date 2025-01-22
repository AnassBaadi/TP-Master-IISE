def safe_division(a, b):
    try:
        S = a/b
        print(f"le resultat: {S}.")
    except ZeroDivisionError:
        print("Erreur: Division par zero")
    else:
        print("la division a été effectuée avec succès")
    finally:
        print("La Fonction a été terminé avec succès")
if __name__=='__main__':
    safe_division(1,0)