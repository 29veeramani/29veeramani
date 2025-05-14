#Write a program to find the intersection of two sets.
set1={1,2,3,4,5}
set2={1,4,6,7,8}
def intersection(set1, set2):
    return set1 & set2
out=set1 & set2
print(out)