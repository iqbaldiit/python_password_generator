'''
This module is for input validation and other common functions
In this system we will validate
1. number validation : minimum 5 number exists
2. alphabet validation: minimum 10 letter exists
3. special character: avoid comma.  
'''
import re 

number_limit=5
alphabet_limit=10

# Start Validations
def validate_number_limit(item_numbers):
    if len(item_numbers)<number_limit:
        return "Your word must have at least "+str(number_limit)+" number."
    else:
        return ""

def validate_alphabet_limit(items):
    if len(items)<alphabet_limit:
        return "Your word must have at least "+str(alphabet_limit)+" number."
    else:
        return ""

def validate_special_character(items):
    if "," in items:
        return "Comma separated value is not excepted!"
    else:
        return ""     

def validate_email(email):
     if re.search('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$',email):
         return ""
     else:
         return "Please provide valid email address!"

# End of Validations

def word_separation(items):
    num=''.join(re.findall(r'[\d]+',items))
    alphabets=''.join(re.findall(r'[a-zA-Z]', items))
    return [num,alphabets]

def error_message(msg):
    if msg!="":
        print(msg)
        exit()