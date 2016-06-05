import random

# -----------nxm boyutunda rastgele matris oluşturma--------
def createMatris(satir_size,sutun_size):
    matris = []
    satir_array = []

    for i in range(0,satir_size):
        for j in range(0,sutun_size):
            satir_array.append(int(random.uniform(0,10)))
        matris.append(satir_array)
        satir_array = []
    return matris
    
#-----------------------------------------------------------

# -------------iki matris çarpimi---------------------------
def matriscarp(matris1,matris2):
	
	for i in range(0,len(matris2)): # matris2'nin sütun sayısını bulmak için
		sutun_sayisi = matris2[i]
	
	matris3=[]
	temp=[]
	temp2=[]
	
	su = len(sutun_sayisi)	 #matris2 nin sütun sayısı	
	sa = len(matris1)		 #matris1 in satır sayısı
	sa2 = len(matris2)       #matris2 in satır sayısı
	
	for x in range(0,sa):
		
		for i in range(0,su):

			for a in range(0,sa2):
				temp.append(matris1[x][a]*matris2[a][i])
			sayi = 0
			for t in temp:
				sayi = sayi + t
			temp2.append(sayi)
			temp = []
			
	for a in range (0,sa):
		temp=[]
		for i in range (0,su):
			kac = a*su + i
			temp.append(temp2[kac])
		matris3.append(temp)
			
	return matris3
#---------------------------------------------------------				

	
matris1=createMatris(2,2)
matris2=createMatris(2,4)

for i in matris1:
    print (i)
print("------------------\n")

for i in matris2:
    print (i)
print("------------------\n")


matris4 = matriscarp(matris1,matris2)	

print("--matris carpimi--\n")	
for i in matris4:
    print (i)
print("------------------\n")
  
            
                
                    
    
  
