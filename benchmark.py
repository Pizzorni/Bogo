import time
import copy
import random
import sort

def main():
	#x = random.sample(range(1000),5)
	x = random.sample(range(1000),10)
	#x = random.sample(range(1000),50)  # Run overnight
	#x = random.sample(range(1000),100) # Do not run unless on super computer
	y = copy.copy(x)
	z = copy.copy(x)

	format = "{0:.3f}"
	if(len(x) == 5):
		format = "{0:.6f}"


	t0 = time.time()
	x.sort()
	t1 = time.time()
	normsort = t1-t0
	print("Python sort: " + "{0:0.6f}".format(normsort) + " seconds")

	t2 = time.time()
	sort.Bogosort(y)
	t3 = time.time()
	bogotime = t3-t2
	print("Bogosort: " + format.format(bogotime) + " seconds")

	t4 = time.time()
	sort.Bogobogosort(z)
	t5 = time.time()
	bogobogotime = t5-t4
	print("Bogobogosort: " + format.format(bogobogotime) + " seconds")


main()