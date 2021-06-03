import password_generator as ps
import character_dictionary as cd
import library as lib


#variable declaration
return_value=""
word=""

email=input("Login by email:")

#Common validation for empty value
if email.strip()=="":
    print("Please enter valid password!")
    exit()

#email validation
lib.error_message(lib.validate_email(email))

#Taking user input
intent=int(input("For creating password press 1 \nor for searching password press 2: "))

if intent==1:
    word = input("Enter your word: ")
else:
    word=input("Enter your word or hints: ")

#Common validation for empty value
if word.strip()=="":
    print("Please enter a word for password!")
    exit()

#check comma validation
if intent==1:
    lib.error_message(lib.validate_special_character(word))

#segregate the User Input
word_list=lib.word_separation(word) #return [number,alphabet]

#check number validation
if word_list[0]!="" and intent==1:
    lib.error_message(lib.validate_number_limit(word_list[0]))

#check alphabet validation    
if word_list[1]!="" and intent==1:
    lib.error_message(lib.validate_number_limit(word_list[1]))

#Generate Password
Gen_Pass=ps.Password(word,email);
if intent==1:
    print(Gen_Pass.generate_password())
else:
    print(Gen_Pass.search_password())

