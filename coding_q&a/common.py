#1.factorial of give number?

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
fa=fact(3)
print(fa)