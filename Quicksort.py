import random

def createAnArray(size): 
    import random
    array=[]
    for i in range(0,size):
        array.append(int(random.uniform(-1000,1000)))
    return array


def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


sayac=0
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)
   global sayac
   return sayac

def quickSortHelper(alist,first,last):
  
   if first<last:
    
       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
           global sayac
           sayac=sayac+1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
           global sayac
           sayac=sayac+1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


size=int(input("dizinin boyutu ne olsun"))
array1=[]
import random
for i in range(0,size):
    array1.append(random.randint(-10,10))

print("dizinin boyutu : ",len(array1))
print("dizinin elemanları ")
for i in range(0,size):
    print(i,".  ",array1[i])
    
import time
start_time1=time.time()
print("quick sort  sonucu :", quickSort(array1))
print("gecen süre : ", time.time()-start_time1)
