class NegativeAgeError(Exception):
    pass

def set_age(age):
    if(age<0):
        raise NegativeAgeError("l'age ne peut pas etre negatif")

if __name__=='__main__':
    try :
        set_age(-21)
    except NegativeAgeError as e:
        print(e)