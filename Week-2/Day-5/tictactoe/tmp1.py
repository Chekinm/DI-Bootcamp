def aaa (a,*args, b=40,**kwargs):
    print (a)
    print(b)
    print(args)
    print(kwargs)
   
print(aaa(1, 2,3,4,b=3, k=3,d=7))
