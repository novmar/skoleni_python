class Roman:
    def __init__(self,value):
        if isinstance(value,str):
            self._numeral=value
        elif isinstance(value,int):
            self._numeral= "I" * value
    def __str__(self):
        return self._numeral
    def __repr__(self):
        return f"Roman({self._numeral!r})"
    def __eq__(self, other):
        return self._numeral == other._numeral
    def __add__(self, other):
        #Roman
        return Roman(self._numeral.join(other._numeral))


assert Roman(3) == Roman("III")
assert Roman("I") + Roman(2) == Roman(3)
print(Roman("III")+Roman(5))
a=Roman("III")
b=Roman(3)
print(a)
print(b)

