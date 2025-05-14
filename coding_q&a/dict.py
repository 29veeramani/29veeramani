#1.combine two dict
a={"a":1,"b":2,"c":3}
b={"d":4,"e":5}
a.update(b)
print(a)
#Method_2 its create new dict:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {**dict1, **dict2}
print(merged)

#2.given 2 list covert to dict
lst_1=["name","age","city"]
lst_2=["veera",26,"pkt"]
#out=dict(zip(lst_1,lst_2))
#print(out)

#METHOD_2

ou={lst_1[i]:lst_2[i] for i in range(len(lst_1))}
#print(ou)

#method_3
em={}
for i in lst_1:
    for j in lst_2:
        em[i]=j
        lst_2.remove(j)
        break
#print(em)


