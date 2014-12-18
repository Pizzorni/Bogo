import random

def main():
	x = random.sample(range(1000),100)
	print(x)
	print(Bogobogosort(x))


def Bogosort(list):
	while(not isSorted(list)):
		random.shuffle(list)
	return list

def Bogobogosort(list):
	index = 2
	while(not isSorted(list)):
		Bogosort(list[:index])
		index += 1
		if(not isSorted(list[:index])):
			random.shuffle(list)
			index = 2
	return list




def isSorted(list):
	prev = None
	for x in list:
		if(prev != None and (prev > x)):
			return False
		prev = x
	return True

main()