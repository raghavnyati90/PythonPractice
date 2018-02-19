# test_str = "My name is raghav"

# test_list = test_str.split(" ")
# i = len(test_list)
# a = test_list[::-1]

# print ' '.join(a)

import threading, random

def Splitter(words):
	mylist = words.split()
	newlist = []
	while(mylist):
		newlist.append(mylist.pop(random.randrange(0, len(mylist))))
	print(' '.join(newlist))

if __name__ == '__main__':
	sentence = "I am a handsome beast. World."
	numOfThreads = 5
	threadList = []

	print("Starting")
	for i in range(numOfThreads):
		t = threading.Thread(target=Splitter, args=(sentence,))
		t.start()
		threadList.append(t)

	print("\n thread Count: " + str(threading.activeCount()))
	print("Exiting... \n")

