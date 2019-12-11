# while True:
#     x=int(input("zadej cislo"))
#     if x>0 :
#         print ("Kladne")
#     elif x<0 :
#         print ("zaporne")
#     elif x==0 :
#         print ("nula")

# a=[1,2,3,4,5,0,-3]
# b=[1,2,3,4,5]
# #


#faktorial

# a=1
# n=10
# for i in range(1,n):
#     a*=i
#     print(a)
import itertools, time

class FactorialSeq:

    def __init__(self):
        self.a=1
        self.i=1

    def __iter__(self):
        return self

    def __next__(self):
        self.a*=self.i
        self.i+=1
        return(self.a)


# fact_seq()


# seq = FactorialSeq()
# for item in seq:
#     print(item)
#     time.sleep(1)

## fibonacci
## 1 1 2 3 5 8

a,b = 1,1

# while True:

    # print(a)
    # a,b=b,a+b

    # time.sleep(1)
class fibb:
    def __init__(self):
        self.a=1
        self.b=1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b ,self.a +self.b
        return a


# fib=fibb()
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))

def print_prime():
    for n in itertools.count(2):
        for i in range(2,int(n/2)):
            if n % i ==0:
                break
        else:
            print(n)
            time.sleep(1)
print_prime()

