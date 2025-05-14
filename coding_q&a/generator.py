def demo():
    n=1
    while (n <=10):
        val=n*n
        yield val
        n +=1
a=demo()
for i in a:
    print(i)


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