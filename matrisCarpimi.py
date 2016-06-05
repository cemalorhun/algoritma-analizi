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
	
	for i in range(0,len(matris1)): # matris2'nin sütun sayısını bulmak için
		sutun_sayisi = matris1[i]
		
	for i in range(0,len(matris2)): # matris1'nin sütun sayısını bulmak için
		sutun_sayisi2 = matris2[i]
	
	matris3=[]
	temp=[]
	temp2=[]
	
	su = len(sutun_sayisi)	 #matris1 nin sütun sayısı	
	su2 = len(sutun_sayisi2) #matris2 nin sütun sayısı
	sa = len(matris1)		 #matris1 in satır sayısı
	sa2 = len(matris2)       #matris2 in satır sayısı
	
	if su != sa2:
		print("iki matrisin çarpılabilmesi icin ilk matrisin sutun sayisi ikinci matrisin satir sayisina esit olmalidir")
	else:
		for x in range(0,sa):
		
			for i in range(0,su2):
	
				for a in range(0,sa2):
					temp.append(matris1[x][a]*matris2[a][i])
				sayi = 0
				for t in temp:
					sayi = sayi + t
				temp2.append(sayi)
				temp = []
			
		for a in range (0,sa):
			temp=[]
			for i in range (0,su2):
				kac = a*su2 + i
				temp.append(temp2[kac])
			matris3.append(temp)
				
		print("--matris carpimi--\n")	
		for i in matris3:
			print (i)
			 
		print("------------------\n")
	
	
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


  
            
                
                    
    
  
