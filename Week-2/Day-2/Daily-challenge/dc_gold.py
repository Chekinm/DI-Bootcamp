        # The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.
# Bonus : If they were born on a leap year, display two cakes !
happy = [0,0,0,0,0,0,0]

happy[0] =     '      |             |      '
happy[1] =     '      | :H:a:p:p:y: |      '
happy[2] =     '  ____|_____________|____  '
happy[3] =     '  |                     |  '
happy[4] =     '  |  :B:i:r:t:h:d:a:y:  |  '
happy[5] =     '  |                     |  '
happy[6] =     '  |_____________________|  '

# some predefined strings

inp = input('Pleasr enter you date of birth!(DD/MM/YYYY): ')

year = int(inp[-4:])
l_dig = year % 10
if l_dig == 0:
    l_dig = 10  # 0 candle is too silly
    # by the way %11 will also do the trick

# just usual condition for leap years
is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

# create string with candles
# to be simmetric, I add underscore in the middle in case of 
# even number of candels

candle = ('      '+'_'*((15-l_dig)//2) + 'i' * (l_dig//2) +
       ('i' if l_dig % 2 else '_') + 
       'i' * (l_dig//2) + '_'*((15-l_dig)//2)+'      ')


# now we have evrything to print. let's go
print('')
print('')
print('')

print( candle + ' '+ is_leap * candle)
for hp in happy:
    print(hp, is_leap * hp)

print('')
print('')
print('')


