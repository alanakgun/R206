import sys

def divide(a:float, b:float)-> float:
    c = a/b
    return c
def divide2(a,b):
    if b!=0:
        c = a/b
        return c
    else:
        print("Division par zéro")

def divide3(a,b):
    try:
        c = a/b
    except ZeroDivisionError as e:
        print(f" Zero :\t {e}")
    except TypeError as a:
        print(f"Type \t : {a}")
    except Exception as t:
        print(t)
    else:
        return c
def main():
    flag = False
    while(not flag):
        try:
            a = float(input("Saisir le dividende"))
        except ValueError:
            print(f"Saisir une valeur réelle")
        else:
            flag=True

flag = False
while (not flag):
    try:
        b = float(input("Saisir la diviseur"))
    except ValueError:
        print("saisir une valeur réelle")
    else:
        flag = True
    #c = divide(a,b)
    c = divide3(a,b)
    if c is not None:
        print(f"Affiche la division de {a} par {b} vaut {c}")


if __name__=="__main__":
    sys.exit(main())