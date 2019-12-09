# 10 cisel,  vypsat aritmeticky prumer
# a=0
# for _ in range(10):
#     a+=int(input("zadejte cislo"))
# print(a/10)
# pole=[]
# pocet=4
# celkem=0
# pomalu=0
# for i in range(1,pocet + 1 ):
#     cislo=int(input(f"Zadej X{i}"))
#     pole.append(cislo)
#     celkem+=cislo
#
# print (pole)
# for i in pole:
#     pomalu+=i
#     print(i)
#
# print (f"{celkem/pocet}")
# print (f"{pomalu/pocet}")
#
# def kolikrat():
#     """Vratmi ti input osetrey >0 a cislo
#
#     ...
#     ...
#     """
#     while True:
#         try:
#             pocet=int(input("kolik bude cisel: "))
#             if not pocet>0:
#                 raise ValueError(f"Count musi byt lepsi {pocet}")
#             return pocet
#         except ValueError as e:
#             print(f"Badinput {e}")


def kolikrat:
    while True:
        try:
            x=int(input("dej cislo"))
        except ValueError
            break


count=kolikrat()
cislo=0
for i in range(count):
    cislo+=int(input(f"Zadej X{i+1}"))

print (f"{cislo/count}")
