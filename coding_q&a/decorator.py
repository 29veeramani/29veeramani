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