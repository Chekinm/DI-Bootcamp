# Instructions
# Create a class called Phone. 
# This class takes a parameter called phone_number. 
# When instantiating an object create an attribute called 
# call_history which value is an empty list.

class Phone():
    
    abonents = []

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []
        Phone.abonents.append(self)

# Add a method called call that takes both self 
# and other_phone (i.e another Phone object) as parameters. 
# The method should print a string stating who called who, 
# and add this string to the phone’s call_history.
    def call(self, caller):
        print(f'{caller.phone_number}  calls to {self.phone_number}')
        self.call_history.append(caller.phone_number)
# Add a method called show_call_history. This method should print the call_history.
    def show_call_history(self):
        print(self.call_history)

# Add another attribute called messages to your __init__() 
# method which value is an empty list.

# Create a method called send_message which is
# similar to the call method. Each message should be saved 
# as a dictionary with the following keys:
# to : the number of another Phone object
# from : your phone number (also a Phone object)
# content
    def send_message(self, caller_to, content):
        self.messages.append({'to': caller_to.phone_number,
                              'from':self.phone_number,
                              'content':content
                            })
        caller_to.messages.append ({'to': caller_to.phone_number,
                              'from':self.phone_number,
                              'content':content
                            })
        
    def show_outgoing_messages(self):
        outgoing_msg = []
        for message in self.messages:
            if message['from'] == self.phone_number:
                outgoing_msg.append(message)
        print(outgoing_msg)
        

    def show_incoming_messages(self):
        incoming_msg = []
        for message in self.messages:
            if message['to'] == self.phone_number:
                incoming_msg.append(message)   
        print(incoming_msg)

    def show_messages_from(self, caller):
        incoming_from = []
        for message in self.messages:
            if message['from'] == caller.phone_number:
                incoming_from.append(message)   
        print(incoming_from)

        
# Create the following methods: show_outgoing_messages(self), 
# show_incoming_messages(self), show_messages_from(self)

# Test your code !!!

caller1 = Phone('11111')
caller2 = Phone('22222')
caller3 = Phone('33333')
caller4 = Phone('44444')

from random import choice

for i in range(55):
    ab1 = choice(Phone.abonents)
    ab2 = choice(Phone.abonents)
    while ab2 == ab1:
        ab2 = choice(Phone.abonents)
    ab1.call(ab2)
    ab2.send_message(ab1, str(i)*2)

caller1.send_message(caller2,'hi. whats up?')


print(caller1.call_history)


print('\n\n')
caller1.show_outgoing_messages()
print('\n\n')
caller1.show_incoming_messages()
print('\n\n')
caller1.show_messages_from(caller3)



    



