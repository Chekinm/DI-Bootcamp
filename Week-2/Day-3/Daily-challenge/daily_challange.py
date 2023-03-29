# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
# Examples


word = input('Enter a word: ')

my_dict ={}
for i, char in enumerate(word):
    if char not in my_dict:
        my_dict[char]=[i]
    else:
        my_dict[char].append(i)
    
print(my_dict)




# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# 


def usd_to_num(usd):
    num = []
    for char in usd:
        if char.isnumeric():
            num.append(char)
    return int(''.join(num))

def what_can_i_buy(items_purchase, wallet):
    
    for key in items_purchase:
        items_purchase[key] = usd_to_num(items_purchase[key]) 
    
    wallet_num = usd_to_num(wallet)
    
    purchased = []

    while items_purchase and wallet_num:
        max_p = max(items_purchase, key=items_purchase.get)
        if wallet_num >= items_purchase[max_p]:
            wallet_num -= items_purchase[max_p]
            purchased.append(max_p)
            items_purchase.pop(max_p)
        else:
            items_purchase.pop(max_p)

    return sorted(purchased) if purchased else 'Nothing'

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"

print(what_can_i_buy(items_purchase, wallet))

items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$10",
  "Spoon": "$2"
}

wallet = "$100"

print(what_can_i_buy(items_purchase, wallet))


items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$1" 

print(what_can_i_buy(items_purchase, wallet))
