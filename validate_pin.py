def validate_pin(pin):
#checks if submitted pin has 4 or 6 characters and if its a string and not a string
    if (pin.isdigit() and(len(pin)==4 or len(pin)==6)):
            
        return True
    else:
        return False



#an alternative way using regex
 import re

def validate_pin(pin):
    return bool(re.match(r'^(?:\d{4}|\d{6})$', pin))