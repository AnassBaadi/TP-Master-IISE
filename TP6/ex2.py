def convert_to_int(value):
    try :
        print(int(value))
    except ValueError:
        print("conversion echoue")
convert_to_int("42")
convert_to_int("1Hell0")
convert_to_int(3.14)