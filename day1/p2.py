#
from collections import Counter

text_file = open("input.txt","r")
lines = text_file.readlines()
lines = list(map(int, lines))


f=0
f_list = [0]
s = set(f_list)
while True:
	for num in lines:
		f+=num	 	
		if (f in s):
			print(f)
			#f_list.append(f)
			#print (f_list)
			quit()
		else:
		 	s.add(f)

	#print("size of list: ",len(f_list))
	