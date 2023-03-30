import numpy

def neo_decript(text :str)->str:
    """decode strange NEO chippr"""
    is_between = 0
    text_as_list = []
    
    #create 2- dimention matrix with character from text
    matrix = [[char for char in string] for string in text.split('\n')]

    # iterate perpendiculary main axis and select alpha numeric sumbol to add to decoded list 
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[j][i].isalpha():
                if is_between > 1:
                    text_as_list.append(' ')
                    is_between = 0
                text_as_list.append(matrix[j][i])
            else:
                is_between += 1
    return ''.join(text_as_list).strip()

# incoming data

text ="""7i3
Tsi
h%x
i #
sM 
$a 
#t%
^r!"""

print(neo_decript(text)) 


    
