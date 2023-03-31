hello
# my_list=["a", "b", "c", "d",1,2,3,4]
# print(type(my_list))
# print(len(my_list))
# i=len(my_list)-1
# print(my_list[i])
# a=['p','r','o','b','e','f']
# i=len(a);
# j=len(a)-3
# new_list=a[j:i]
# # print(new_list)
# # print(a[-j:])
# # print(a)
# # a[1]='q'
# # print(a)
# # a[0:3]=['apple','cat','cheese']
# # print(a)
# # i=len(a)-3
# # print(a)
# a[j:]=['apple','cat','cheese']
# print(a)
# a.append("a")
# a.extend(['b','c','d'])
# a.insert(4,"insert")
# a.__delitem__(-1)
# # a.__delitem__(new_list)
# print(a)
# #the remove method  remove an element from the list
# #it takes an list item as parameter
# #output is ['p', 'r', 'o', 'insert', 'cat', 'cheese', 'a', 'b','c]
# a.remove("apple")
# print("remove",a)
# #the pop method remove the last element of a list
# #output is ['p', 'r', 'o', 'insert', 'cat', 'cheese', 'a', 'b']
# a.pop()
# print("pop",a)
# #the index method return the index of list item which is passed to the method
# #output is 4
# index=a.index('cat')
# print("index",index)
# #this method returns how many times a item is occured in list
# #output is 1
# count=a.count('insert')
# print("count",count)
# #this method sort the list items either ascending or descending order
# #output is ['r', 'p', 'o', 'insert', 'cheese', 'cat', 'b', 'a'] and ['a', 'b', 'cat', 'cheese', 'insert', 'o', 'p', 'r'] in  descending
# #and ascending order respectively
# rsort=a.sort(reverse=True)
# print("reverse sort",a)
# sort=a.sort()
# print("sort",a)
# #this method arrange the list item in descending order
# #same as sort with reverse
# #output is ['r', 'p', 'o', 'insert', 'cheese', 'cat', 'b', 'a']
# a.reverse()
# print("reverse",a)
# #clear method remove all the items of list
# #output is[]
# a.clear()
# print("clear",a)
# # remove,pop,clear,index,count,sort,reverse

# #tupple
# my_tupple=('a','b','c','d','e','f','g','h')
# print("tupple",my_tupple)
# print(type(my_tupple))
# print(len(my_tupple))
# my_list=['a']
# print(type(my_list))
# my_tuple=('a',)
# print(type(my_tuple))
# x=('a','b','c','d','e','f','g','h')
# # (a,b,c)=x
# (a,b,*c)=x
# print(a)
# print(b)
# print(c)
# print(type(c))

# set
# my_set={'a','b','c','a'}

# print(type(my_set))
# print(my_set)
# a=['a','b','c','d','1','2','a','b','c','d']
# my_set=set(a)
# my_set.add("e")
# print(my_set)
# my_set.update({
#     "f","g"
# })
# my_set.remove('a')
# b=list(my_set)
# c=my_set.discard('z')
# print(c)
# print(b)
# a={'a','b','c','d','1','2','a'}
# b={'c','x','y','b','z'}
# c=a.intersection(b)
# print(c)
# a=['1','2','3','4','5','6','7','a','b','c',]
# b=['1','2','3','a','b','c','d','e','f']
# c=set(a)
# d=set(b)
# e=c.intersection(d)
# print(f"the common element in the list {a} and {b} is",list(e))
# string
# myString=input("Enter a string")
# print(myString[-3])
# print("length of string is ",len(myString))
# b=myString.split(' ')
# print(len(b))

# c=input("Enter word to count occurrences")

# print(b.count(c))
# my_list=['a','b','c','d','e',]
# my_list.append("x")
# my_list.extend(['y','z','1','a'])
# i=len(my_list)
# j=i-4
# a=my_list[j:i]
# a[:2]=["cat","dog"]
# print(i,j)

# a.reverse()
# print(a)
# my_list.sort(reverse=True)
# my_list.insert(0,"inserted")

# print(my_list)
# my_tuple=("a","b","c","d","e")
# x=my_tuple.__contains__("a")
# (x,y,*z)=my_tuple
# print(z)
# print(my_tuple)
# my_set={'a','b','c','d','e','1',}
# secondset={'x','y','z','1','a'}
# myList=list(my_set)
# myTupple=tuple(my_set)
# # print(myList)
# # print(myTupple)
# # my_set.add("x")
# d=my_set.intersection(secondset)

# print(d)
# print(my_set)

my_dic = {
    "fname": "Devraj",
    "lname": "Shrestha",
    "address": {
        "permanent": "Bhojpur",
        "temporary": "Dharan"
    },
    "education": {
        "complete": "+2",
        "running": "Bachelor"
    },
    "school": {
    "lower":"Panchakanya",
    "+2":"Bishwopremi",
    "see":"Bishwopremi",
    "bachelor":"BMC"
    }
}
print("name:",my_dic["fname"] + " "+ my_dic['lname'])
print("Permanent address:",my_dic["address"]["permanent"])

