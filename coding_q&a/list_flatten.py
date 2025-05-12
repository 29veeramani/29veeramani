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


def outer(fucn):
    def inner(fname,lname):
        result=fucn(fname,lname)
        return result.upper()
    return inner
@outer
def st(fname , lname):
    return fname+lname
#fname="veera"
#lname="mani"
out=st("veera","mani")
print(out)

def demo():
    n=1
    while (n <=10):
        val=n*n
        yield val
        n +=1
a=demo()
for i in a:
    print(i)



















