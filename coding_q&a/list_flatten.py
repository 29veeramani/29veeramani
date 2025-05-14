#1.flatten the nested  given list?

lst=[1, [2, [3, 4], 5], 6]
out=[]
for i in lst:
    if isinstance(i,list):
        for j in i:
            if isinstance(j,list):
                for k in j:
                    if isinstance(k,list):
                        for l in k:
                            out.append(l)
                    else:
                        out.append(k)
            else:
                out.append(j)
    else:
        out.append(i)

#print(out)
#method_2

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

nested =[1, [2, [3, 4], 5], 6]
flat = flatten(nested)
print(flat)

#2.remove dupligate in the list?
#Method_1:
dup=[1,3,5,7,9,3,3,5]
dup=list(dict.fromkeys(dup))

#Method_2
dup=list(set(dup))
#print(dup)

#Method_3:
ans=[]
val=[]
for i in dup:
    if i not in ans:
        ans.append(i)
    else:
        val.append(i)
#print(val)

#3.How many occurance repeated  in the list?
l=[1,3,5,7,9,3,3,5,7,7,7,9]
freq={}
for i in l:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] = 1
#print(freq)

#4.find the maxi 5 numbers in list?
#method_1
lst_1=[1,2,3,4,5,6,7,8]
#lst_1.sort(reverse=True)
#print(lst_1[:5])

#Method_2
out_1=[]
for i in range(5):
    maximum = max(lst_1)
    out_1.append(maximum)
    lst_1.remove(maximum)
#print("maximum:",out_1)


#5.reverse the list ?
#Method_1:
my_list = [1, 2, 3, 4, 5]
revers=[]
for i in range(len(my_list),-1,-1):
    revers.append(i)
#print(revers)

#Method_2
my_list_1 = [1, 2, 3, 4, 5]
#print(my_list_1[::-1])
my_list_1.reverse()
#print(my_list_1)

#6.find the maximum value in the list
#method_1
l = [1, 2, 3, 4, 5]
#print(max(l))

#method_2
l.sort(reverse=True)
#print(l[1])

#7.Write a program to find the common elements in two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
com=list(set(list1)&set(list2))
#print(com)
#Method_2
lt=[]
for i in list1:
    if i in list2:
        lt.append(i)
#print(lt)

#8.How do you find the length of a list without using the len() function?
my_list_3 = [10, 20, 30, 40]

count = 0
for _ in my_list_3:
    count += 1

print("Length of the list:", count)


























