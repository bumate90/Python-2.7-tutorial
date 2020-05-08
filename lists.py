#In python the lists can store different types of elements
#And the elements do not have a set size
#initialize
my_list = []
my_list2 = [1, 2, 3, ":)", True, 4.5]

#add item
my_list2.append(88)
print my_list2

#access elements
print my_list2[3]

#change elements
my_list2[3] = ":DxDxDxD"
print my_list2[3]

#remove element by index
del my_list2[3]

#iterate
for element in my_list2:
	print element
