def demo():
    n=1
    while (n <=10):
        val=n*n
        yield val
        n +=1
a=demo()
for i in a:
    print(i)