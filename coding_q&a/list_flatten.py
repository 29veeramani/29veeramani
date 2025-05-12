#flatten the nested  given list?

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

print(out)

#2.remove dupligate in the list?
#Method_1:
dup=[1,3,5,7,9,3,3,5]
dup=list(dict.fromkeys(dup))

#Method_2
dup=list(set(dup))
print(dup)

#Method_3:
ans=[]
val=[]
for i in dup:
    if i not in ans:
        ans.append(i)
    else:
        val.append(i)
print(val)

#How many occurance repeated  in the list?
l=[1,3,5,7,9,3,3,5,7,7,7,9]
freq={}
for i in l:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] = 1
print(freq)

#find the maxi 5 numbers in list?
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



























