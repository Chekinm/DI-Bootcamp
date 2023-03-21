for i in range(16):
    for k in range(16):   
        print('<p class=\"col' + str(2 * (i % 2) + k % 2 + 1) + ' block\"></p>')
