l1=[1,2,3,4,4,3,2]
l2=[1,2,3,4]
d={}
for k in l1:
    if k in d:
        d[k] +=1
    else:
        d[k]=1
print(d)

n=int(input("enter the number"))
count=1
for i in range(1,n):
    if n%i==0 :
        count +=1
if count==1:
    print("prime")
else:
    print("not prime")

