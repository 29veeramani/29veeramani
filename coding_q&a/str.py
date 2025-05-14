#1.how to reverse each word?

st="hello friends"
new=""
for i in st:
    new=i+new
#print(new)
#method_2
#print(st[::-1])

#2 check given strings are palindrom?

s="amma"
s_1=s[::-1]
if s==s_1:
    print("yes")
else:
    print("no")

#3how to seprate string characters based on the odd even position?

w="veeramani"
odd=""
even=[]
for i in range(len(w)):
    if i%2==0:
        even.append(w[i])
    else:
        odd=odd+w[i]
#print(str(odd))
#print(str(even))
#method_2

#print("even:",w[::2])
#print("odd:",w[1::2])