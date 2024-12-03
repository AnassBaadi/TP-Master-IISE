def salutation(nom,salut='Bonjour'):
    return salut+' '+nom
nom=input('Veuillez Saisir votre nom : ')
Sal=input('Veuillez Saisir votre Salutation Preferee, sinon tapez rien : ')
if Sal=='':
    print(salutation(nom))
else:
    print(salutation(nom,Sal))