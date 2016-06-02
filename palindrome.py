def palindrome(dizi):
	for i in range(len(dizi)):
		for j in range(len(dizi)):
			dizi2=dizi[i][j]
			dizi2Ters = dizi2[::-1]
			if dizi2 == dizi2Ters:
				print(dizi2)
			
liste = [["ada","1251"],["runnur","cemal"]]
palindrome(liste)
