import random

def hash_create(sayi):
	rand = int(random.uniform(0,10))
	sayi = sayi + rand
	rand2 = int(random.uniform(0,10))
	sayi = sayi%rand2
	cemal = "cemalorhunbakan"
	new_str = cemal[rand:rand2]
	sayi = str(sayi)
	new_number = sayi + new_str
	print(new_number)

hash_create(5)
