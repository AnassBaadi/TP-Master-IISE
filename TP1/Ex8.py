def somme_varargs(*args):
    s=0
    for i in args:
        s=s+i
    return s
print(somme_varargs(2,4,5,6,7))