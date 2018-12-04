#
text_file = open("input.txt","r")
lines = text_file.readlines()
lines = list(map(int, lines))

f=sum(lines)
print (f)

