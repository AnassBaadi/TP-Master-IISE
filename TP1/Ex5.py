def factorielle(n):
    if n==1: return 1
    return n*factorielle(n-1)
n=int(input('Saisir un entier : '))
print(factorielle(n))