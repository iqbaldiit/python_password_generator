import random
import sys
import character_dictionary as cd
import db_helper as db

#random.choice(string.ascii_letters)

class Password:
    def __init__(self, word):        
        self.word = word

    def generate_password(self): 
        medium=""
        strong=""
        very_strong=""

        try:
            #Generate Password
            for x in range(len(self.word)):
                medium = medium + random.choice(self.word)  
                strong = strong + random.choice(self.word)+random.choice(cd.NUMBERS)+random.choice(str(self.word).upper()) 
                very_strong=very_strong+random.choice(self.word)+random.choice(cd.NUMBERS)+random.choice(str(self.word).upper())+random.choice(cd.SPECIAL_CHARACTERS) 
            
            medium=list(medium)
            strong=list(strong)
            very_strong=list(very_strong)
            random.shuffle(medium)
            random.shuffle(strong)
            random.shuffle(very_strong)
            
            dct_password={"Word":self.word,"Medium": "".join(medium),"Strong":"".join(strong),"Very_strong":"".join(very_strong)}

            #Insert to csv file
            db.insert_update(dct_password)
            return dct_password
        except:
            print("Opps!", sys.exc_info()[0], "occured.")

    def search_password(self):
        uInput=str(self.word).lower() 
        fileData=db.read()

        search_result=[]
        for r in fileData:
            if uInput in r[0].lower():             
                search_result.append({"Word":r[0],"Medium": r[1],"Strong":r[2],"Very_strong":r[3]})           
        
        search_result=[lst for lst in search_result if lst!=[]]
        search_result="Opps! Not matched, try again" if search_result==[] else search_result
        return search_result

