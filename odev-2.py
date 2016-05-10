import random
import time

def DiziOlustur(myArray, uzunluk):
     myArray = random.sample(range(1, 10000000), uzunluk)
    return myArray
    
def BinarySearch(myArray, number):
    en_kucuk = 0
    en_buyuk = len(myArray)
    while en_kucuk < en_buyuk:
        ortanca = en_kucuk + (en_buyuk - en_kucuk) // 2
        ort_eleman = myArray[ortanca]
        if number == ort_eleman:
            return ortanca
        elif number > ort_eleman:
            if en_kucuk == ortanca:
                break
            en_kucuk = ortanca
        elif number < ort_eleman:
            en_buyuk = ortanca

uzunluk = int(input("Dizinin Uzunluğu:"))
myArray = []
DiziOlustur(myArray, uzunluk)
myArray = sorted(DiziOlustur(myArray, uzunluk))
print ("Dizinin Elemanları")
for i in myArray:
    print(i)
number = int(input("Aranacak Numara:"))
start_time=time.time()
print("aranan eleman dizinin ", BinarySearch(myArray, number),". elemanı")
print ("geçen süre: ",time.time()-start_time)
