## 10 / 2 = 5.0



class kalkulacka():
    def __init__(self):
        pass

    def readinput(self):
        while True:
            try:
                self.cislo=float(input("Zadej cislo"))
            except ValueError:
                print("spatne cisloa")
                continue
            return self.cislo

    def deleni(self):
        a=self.readinput()
        b=0
        while b==0:
            b=self.readinput()
        return (f"{a} / {b} = {a/b}")


pocite=kalkulacka()

print(pocite.deleni())

