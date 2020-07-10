examplelist = ["blue","green","orange"]
print(examplelist)
print(examplelist[1])#slicing
print(examplelist[-1])
print(examplelist[1:2])
print(examplelist[1:])
print(examplelist[:2])
examplelist[1]="yellow"
print(examplelist)
for i in examplelist:
    print(i)
print(len(examplelist))
print(examplelist)
examplelist.append("green")
print(examplelist)
examplelist.insert(1,"pink")
print(examplelist)
examplelist.remove("pink")
print(examplelist)
examplelist.pop(1)
print(examplelist)
example_list = ["apple", "banana", "cherry"]
mylist = example_list.copy()
print(mylist) 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2

print(list3) # Output: ["a", "b", "c", 1, 2, 3]

#also possible to create list of constructors
exa = list(("apple", "bannana"))
print(exa)
