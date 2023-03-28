def test(c, a=None):
    if a == None:
        a = []
    
    a.append(c)
    return a

b = [1,2,3]
print(test(4, b))
print(test(4))
print(test(4))
print(test(4))
