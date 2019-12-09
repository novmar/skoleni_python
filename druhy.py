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


seq = FactorialSeq()
for item in seq:
    print(item)
    time.sleep(1)
