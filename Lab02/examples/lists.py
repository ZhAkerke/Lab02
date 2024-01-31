#Python Lists
mylist = ["apple", "banana", "cherry"]

thislist = ["apple", "banana", "cherry"]
print(thislist) #['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) #['apple', 'banana', 'cherry', 'apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #3

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#['apple', 'banana', 'cherry']
#[1, 5, 7, 9, 3]
#[True, False, False]

list1 = ["abc", 34, True, 40, "male"]
#['abc', 34, True, 40, 'male']

mylist = ["apple", "banana", "cherry"]
print(type(mylist)) #<class 'list'>

thislist = list(("apple", "banana", "cherry")) 
print(thislist) #['apple', 'banana', 'cherry']



#Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])  #banana

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #cherry

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #['cherry', 'orange', 'kiwi']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #['cherry', 'orange', 'kiwi', 'melon', 'mango']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #['orange', 'kiwi', 'melon']

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
 print("Yes, 'apple' is in the fruits list") 



#Change List Items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #['apple', 'blackcurrant', 'cherry']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) #['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #['apple', 'blackcurrant', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #['apple', 'watermelon']

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) #['apple', 'banana', 'watermelon', 'cherry']



#Add List Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) #['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) #['apple', 'orange', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) #['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) #['apple', 'banana', 'cherry', 'kiwi', 'orange']



#Remove List Items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #['apple', 'cherry']

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) #['apple', 'cherry', 'banana', 'kiwi']

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) #['apple', 'banana']

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) #['banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
del thislist #Error

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #[]



#Loop Lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 
#apple
#banana
#cherry
  
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) 

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist) #['apple', 'banana', 'mango']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) #['apple', 'banana', 'mango']

newlist = [x for x in fruits if x != "apple"] 
#['banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in fruits]
#['apple', 'banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in range(10)]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

newlist = [x for x in range(10) if x < 5]
#[0, 1, 2, 3, 4]

newlist = [x.upper() for x in fruits]
#['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

newlist = ['hello' for x in fruits]
#['hello', 'hello', 'hello', 'hello', 'hello']

newlist = [x if x != "banana" else "orange" for x in fruits]
#['apple', 'orange', 'cherry', 'kiwi', 'mango']



#Sort Lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)



#Copy Lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)



#Join LIsts
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
