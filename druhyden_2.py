# vstupni parametry ( modifikuji X Nemodifikuju)
# vysledek
# lokalni promenne


# globlani promnenne (bad practice)
# X functional programming + closures

def f(a,b,c):
    """
    suppress.focus.stealing=false
    """
    return 100*a + 10 * b + 1 * c

def f1(a=0,b=0,c=0):
    """
    Nepovinne parametry
    a=0
    b=0
    c=0
print (f1(10,20))
print (f1(a=10,b=20))
Volani jmenem
    """
    return 100*a + 10 * b + 1 * c

'''
print (f1(b=10,a=20))
arg=[1,2]
wargs={"c":3}
f(*arg,**wargs)
'''


def myprint(*arfs):
    print(args)


