#empty list
my_list = []
#append elements 10,20,30,40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#insert 15 at second position 
my_list.insert(1, 15)
#extend list 
my_list.extend([50,60,70])
#remove the last element 
my_list.pop()
#sort the list
my_list.sort()
#find and print the index of value 30
print("final list:",my_list)
index_of_30=my_list.index(30)
print("index of 30:",index_of_30)

