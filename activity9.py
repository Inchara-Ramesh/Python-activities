listone = [3,4,5,6,7]
listtwo = [6,7,8,9,10]
listthree = []

for i in listone:
    if ( i % 2 != 0):
       listthree.append(i)
for j in listtwo:
    if ( j % 2 == 0):
       listthree.append(j)

print(listthree)


