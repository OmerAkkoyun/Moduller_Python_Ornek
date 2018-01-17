import math """ math.(modul ismi) kullanabilirz artýk burdan çaðýrýlcak """
while True:
    sayi=int(input("faktoriyeli hesaplanacak sayiyi gir : "))
    if sayi <0:
        print("sýfýrdan büyük sayý giriniz..")
    else:
        print (math.factorial(sayi))

+++++++++++++++++++++++++++++++++++++++++++
eðer en baþa ; import math
 yerine
from math import *
yazarsak 

modul çaðýrýrken
> math.factorial(5) yerine 
direkt
> factorial(5) yazabiliriz