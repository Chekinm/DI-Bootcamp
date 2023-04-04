# Exercise 1 : Built-In Functions
# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.

# Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.

class PositiveInteger():

    def __init__(self):
        self.value = abs(int(float(input('Enter a float number: '))))
    @property
    def __doc__(self):
        return ('''Positive integer class get the value from imput and convert it to  positive integer using int() and abs built function''')

a = PositiveInteger()
print(a.value)
print(a.__doc__)

# # 🌟 Exercise 2: Currencies
# Instructions
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        ending = 's' if self.amount > 1 else ''
        return(f'{self.amount} {self.currency}{ending}')

    def __int__(self):
        return self.amount  

    def __repr__(self) -> str:
        return str(self)

    def __add__(self, to_add):
        if isinstance (to_add, int):
            return self.amount + to_add
        elif isinstance(to_add, Currency) and to_add.currency == self.currency:
            return self.amount + to_add.amount
        elif isinstance(to_add, Currency):
            raise ValueError (f'cannot add {self.currency} and {to_add.currency}') 
        else:
            raise TypeError (f'cannot add {str(type(self))} and {str(type(to_add))}')


    def __iadd__(self, to_add):
        if isinstance (to_add, int):
            self.amount = self.amount + to_add
            return self
        elif isinstance(to_add, Currency) and to_add.currency == self.currency:
            c_temp = Currency(self.currency, self.amount + to_add.amount)
            return c_temp
        elif isinstance(to_add, Currency):
            raise ValueError (f'cannot add {self.currency} and {to_add.currency}') 
        else:
            raise ValueError (f'cannot add {str(type(self))} and {str(type(to_add))}')



c1 = Currency('dollar', 1)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)


print(c1)
print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
a = c1 + c2
print(a)
c1 += c2
print(c1)
c1 += 3
print(c1)
print(c3)
c4+=c3
print(c4)

