####LIST INTRO
x = [1, 2, 3, 4]
print(x[3])        #index position 3, 4th element
print(x[-1])       #last index
print(x[-3])       #3rd index from the end
print(x[1:3])      #elements in index 1 & 2
print(x[:2])       #elements in index 0 & 1
print(x[1:])       #elements in index 1 to end of list
print(x[-2:4])     #elements in between 2nd index from the end and 3rd index from start
print(x[::2])      #every other element is skipped
print(x[:-2])      #elements in index 0,1
print(x[-2:])      #elements in index 2,3
print(x[::-1])     #reverse
print(x[-1:0:-1])  #elements in index position 3 (last, -1) and index position 1 going left

###LIST & INSERT
a = []             # []
x.insert(0,0)      #insert 0 in index position 0
a.insert(0,1)      # [1]
a.insert(0,2)      # [2,1]
a.insert(0,3)      # [3,2,1]
y = []             # []
y.insert(5,100)    # [100]
print(len(y))      # 1

###LIST & APPEND
x.append(5)        #append 5 at the end

###LIST & DELETE
del x[0:1]         #delete elements in index 0
del x[:]           #delete ALL elements inside x

###SETS
s = set([1,2,3,4])
print(s)   #[1,2,3,4]
s.discard(3)
print(s) #[1,2,4]


#a.sort() Inplace sort
#sorted() returns a new list, works for lists and dict

####Sort List
lucky = ['22', '11', '31']
print(lucky)
lucky.sort(reverse=True)
print("sorted in reverse ...")
print(lucky)
print("~~~~~~~~~")

####
xyz = ['abcd','abcdef', 'abc']
print(xyz)
xyz.sort(key=len,reverse=True)
print("sorted in reverse string length ...")
print(xyz)
print("~~~~~~~~~")

#####List of lists
#Question: Reverse sort by lucky number
people2 = [
    ['Harish', 'Chakravarthy', 22],  #first name, last name, lucky number
    ['Jon', 'Doe', 27],
    ['Foo', 'Bar', 18],
]
print(people2)
#Solution 1
people2.sort(key=lambda x: x[2],reverse=True)
print ("sorted by lucky number in reverse")
print(people2)
print("~~~~~~~~~")
#Solution 2 
from operator import itemgetter            
people3 = sorted(people2,key=itemgetter(2),reverse=True)
print(people3)
print("~~~~~~~~~")
#
#
#Question: Sort by key1 and key2
print(input)
input = [[1,3],[4,6],[10,15],[1,2],[2,9]]
#sort by key1 and then key2
input.sort(key=lambda x:(x[0],x[1]))
print("sorted input ===>", input)
#
###List of dictionaries
#Question: sort by last name
people3 = [
    {'FirstName':'Harish','LastName':'Chakravarthy','Lucky':22},
    {'FirstName':'Jon', 'LastName':'Doe', 'Lucky':27},
    {'FirstName':'Foo', 'LastName':'Bar', 'Lucky':18},
]
print(people3)
people3.sort(key=lambda x: x['LastName'],reverse=True)
print ("sorted by last name in reverse")
print(people3)

#####Tuples
#Question: Given height,base,width as tuples. Sort by base
from operator import itemgetter            
a = [(1, 2, 3), (2, 4, 3), (8, 1, 4)]
b = sorted(a,key=itemgetter(1))
print(b)  #[(8, 1, 4), (1, 2, 3), (2, 4, 3)]
print("~~~~~~~~~")
#
#
#
#
######Dictionaries
a = {}
a['hello'] = 5
a['world'] = 4
a['aa'] = 1
a['abc'] = 10
#Question: Sort by key
for k in sorted(a):
	print(k,a[k])

'''
aa 1
abc 10
hello 5
world 4
'''
#Question: Sort by value
for k in sorted(a, key=a.get):
	print(k,a[k])

