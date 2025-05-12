import re

str="ifarrayandhashanddisctanddata"
out=list(str.split("and"))
print(len(out[:3]))

list_1 = [1, 'a','c',4]
list_2 = [1, 2, 3, 4, 5]
va=list_1+list_2
print(list(set(va)))

import re
patter=re.Match(str,[])
[1,2,3,4,5,6,7,8,9]
		o/p [9,2,7,4,5,6,3,8,1]
		reverse the odd indexed values and leave the even values as it is
query to return only duplicate rows
			ename	dept
			vanitha	CSE
			vanitha	EEE
			vanitha	IT
			balaji	IT
			balaji	CSE
			shiv	CSE


a=[i for i in range(1,10+1) if i%2==0]
print(a)
a="veeraman"
def fuct1(func):
     def inner():
         print("hi welcome")
         name=func()
         return name.upper()
     return inner
@fuct1
def org():
    return a
print(org())

