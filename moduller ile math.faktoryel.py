import math """ math.(modul ismi) kullanabilirz art�k burdan �a��r�lcak """
while True:
    sayi=int(input("faktoriyeli hesaplanacak sayiyi gir : "))
    if sayi <0:
        print("s�f�rdan b�y�k say� giriniz..")
    else:
        print (math.factorial(sayi))

+++++++++++++++++++++++++++++++++++++++++++
e�er en ba�a ; import math
 yerine
from math import *
yazarsak 

modul �a��r�rken
> math.factorial(5) yerine 
direkt
> factorial(5) yazabiliriz