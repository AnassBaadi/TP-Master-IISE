def analyse_texte(texte):
    nbr_mots=1
    nbr_carac=0
    dict={}
    for k in texte:
        if k==' ': 
            nbr_mots=nbr_mots+1
        else :
            nbr_carac=nbr_carac+1
    dict['Nombre de mots']=nbr_mots
    dict['Nombre de Caracteres']=nbr_carac
    return dict
txt=input('Saisir le texte qu on peut analyser : ')
print(analyse_texte(txt))