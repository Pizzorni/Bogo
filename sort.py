import random
import time
import copy

def main():
	x = random.sample(range(1000),10)
	y = copy.copy(x)
	z = copy.copy(x)

	t0 = time.time()
	x.sort()
	t1 = time.time()
	normsort = t1-t0

	t0 = time.time()
	Bogosort(y)
	t1 = time.time()
	bogotime = t1-t0

	t0 = time.time()
	Bogobogosort(z)
	t1 = time.time()
	bogobogotime = t1-t0


	print("Normal sort: " + str(normsort) + "\nBogosort: "
	 + str(bogotime) + "\nBogobogosort: " + str(bogobogotime))


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