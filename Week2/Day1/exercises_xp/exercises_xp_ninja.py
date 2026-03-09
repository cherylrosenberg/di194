# Exercise 1 : Call History
# Instructions
# Create a class called Phone. This class takes a parameter called phone_number. When instantiating an object create an attribute called call_history which value is an empty list.

class Phone:
    def __init__(self, phone_number : Phone):
       self.number = phone_number
       self.call_history = []
       self.messages = []

# Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. The method should print a string stating who called who, and add this string to the phone’s call_history.

    def call(self, other_phone):
        call_history = f"{self.number} called {other_phone.number}"
        print(call_history)
        self.call_history.append(call_history)

# Add a method called show_call_history. This method should print the call_history.

    def show_call_history(self):
        print(self.call_history)

# Add another attribute called messages to your __init__() method which value is an empty list.

# Create a method called send_message which is similar to the call method. Each message should be saved as a dictionary with the following keys:
# to : the number of another Phone object
# from : your phone number (also a Phone object)

    def send_message(self, other_phone: Phone):
        message_string = f"Message sent from {self.number} to {other_phone.number}"
        print(message_string)
        
        msg = {
            "to" : other_phone.number,
            "from" : self.number
        }
        self.messages.append(msg)

# content
# Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)

    def show_outgoing_messages(self):
        for msg in self.messages:
            print(f"To: {msg['to']}")

    def show_incoming_messages(self):
        pass

    def show_messages_from(self, other_number):
        for msg in self.messages:
            if msg['from'] == other_number:
                print(f"Message: {msg}")

# Test your code !!!

my_phone = Phone('0509795258')
my_phone.call(Phone('0502352315'))
#my_phone.show_call_history()
my_phone.call(Phone('0502352315'))
my_phone.show_call_history()
my_phone.send_message(Phone('0502352315'))
my_phone.show_outgoing_messages()
my_phone.show_messages_from(Phone('0502352315'))