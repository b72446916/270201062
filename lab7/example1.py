dict = {"Jon": 15, "Ned":45, "Arya":9, "Catelyn":44, "Bran":10}
for person_name in dict:
	if dict.get(person_name) > 18:
		print(person_name)