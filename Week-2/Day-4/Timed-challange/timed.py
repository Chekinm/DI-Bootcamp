def count_letter(string: str, letter: str) ->int:
    res = 0
    for char in string:
        if char == letter:
            res += 1
    return res

print (count_letter('Programming is cool!', 'o'))
