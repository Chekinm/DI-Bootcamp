def a (x=None):
    if x == None:
        x = []
    x.append('fedya')
    return x

print(a([1,2]))
print(a())
print(a())