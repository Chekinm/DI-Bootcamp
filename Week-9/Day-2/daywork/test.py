def a (var1):
    def b (var2):
        return var1 + var2
    return b

nestfunc = a(10)
print(nestfunc)
print(nestfunc(5))
print(nestfunc(7))


const obj1 = {a:1}
const obj2 = obj1