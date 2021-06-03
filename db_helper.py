import csv
import sys

db_name="db_Password.csv"
db_fields=['email','Word',"Medium","Strong","Very_strong"]

def insert_update(item):
    try:
        with open(db_name, 'a+',newline='') as db:  
            db_writer=csv.DictWriter(db, fieldnames = db_fields) 
            db_writer.writerow(item)
            return "Saved successfully!"
    except:
        print("Opps!", sys.exc_info()[0], "occured.")

def read():
    fileReader=csv.reader(open(db_name))        
    fileData=[row for row in fileReader] #now this is only the list without header
    return fileData
