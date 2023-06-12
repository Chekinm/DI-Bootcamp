x = 123
arr_x = []
str_x = str(x)
str_x = str(x).zfill(len(str_x)+len(str_x)%2)
print(str_x)
for i in range(0, len(str_x)-1,2):
    print([str_x[i],str_x[i+1]])
    arr_x.append([str_x[i],str_x[i+1]])


print(arr_x)
    

from collections
