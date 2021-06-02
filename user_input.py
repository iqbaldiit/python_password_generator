import password_generator as ps
import character_dictionary as cd



intent=int(input("For creating password press 1 or for searching password press 2: "))
word=""
if intent==1:
    word = input("Enter your word: ")
else:
    word=input("Enter your word or hints: ")

if "," in word:
    print ("Comma separated value is not excepted!")
else:
    Gen_Pass=ps.Password(word);
    if intent==1:
        print(Gen_Pass.generate_password())
    else:
        print(Gen_Pass.search_password())

