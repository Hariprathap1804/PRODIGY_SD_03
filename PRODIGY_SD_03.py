import pandas as pd
import numpy as np
from tempfile import NamedTemporaryFile
import shutil
import csv
import os

def create(name,ph,mail,file="Contact.csv"):
    with open(file, 'a', newline='') as csvfile:
        fieldnames = ['Name', 'Phone Number', 'E-Mail ID']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Name':name, 'Phone Number':ph,'E-Mail ID':mail})
    csvfile.close()

def update(n_find,name,ph,mail,file="Contact.csv"):
    filename = file
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    fields = ['Name', 'Phone Number', 'E-Mail ID']
    with open(filename, 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        for row in reader:
            if row['Name'] == str(n_find):
                row["Name"],row['Phone Number'], row['E-Mail ID']= name, ph, mail
            row = {'Name': row['Name'], 'Phone Number': row['Phone Number'], 'E-Mail ID': row['E-Mail ID']}
            writer.writerow(row)
    shutil.move(tempfile.name, filename)
    remove_blank()

def remove_blank():
    with open("Contact.csv", newline='') as in_file:
        with open("Contact1.csv", 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            for row in csv.reader(in_file):
                if any(field.strip() for field in row):
                    writer.writerow(row)

    filename = "Contact.csv"
    f = open(filename, "w+")
    f.close()

    shutil.copyfile("Contact1.csv", "Contact.csv")

    file = 'Contact1.csv'
    if(os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)

def delete(name,file='Contact.csv'):
    try :
        df = pd.read_csv(file, index_col='Name')
        df = df.drop(name)
        df.to_csv(file, index=True)
    except:
        print("Name not Found...!")

def view(name,file='Contact.csv'):
    i = 0
    fields = ['Name', 'Phone Number', 'E-Mail ID']
    with open(file, 'r') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            for row in reader:
                if row['Name'] == str(name):
                    print("Displaying details...")
                    print("Name : ",row["Name"])
                    print("Phone Number : ",row['Phone Number'])
                    print("E-Mail ID : ",row['E-Mail ID'])
                    i = 1
    if i == 0:
        print("Name not Found...!")

print("*****************Contact Management System*****************")

i = 0
res = 0
file = 'Contact.csv'
if not(os.path.exists(file) and os.path.isfile(file)):
    print("File doesnot exist... Creating the file 'Contact.csv'...")
    contact = {'Name':[],'Phone Number':[],'E-Mail ID':[]}
    df = pd.DataFrame(contact)
    df.to_csv("Contact.csv",index=False)

while i == 0:
    try :
        print("ACTIONS\n1.CREATE\n2.UPDATE\n3.DELETE\n4.VIEW\n5.EXIT")
        ch = int(input("Enter your choice : "))
        if ch == 1:
            print("Enter the following details...")
            name = input("NAME : ")
            ph = int(input("PHONE NUMBER : "))
            mail = input("E-MAIL ID : ")
            create(name,ph,mail)
            print("**********Contact has been Created**********")
        
        if ch == 2:
            while res == 0:
                ex_name = input("Enter your existing name to UPDATE : ")
                fields = ['Name', 'Phone Number', 'E-Mail ID']
                with open('Contact.csv', 'r') as csvfile:
                    reader = csv.DictReader(csvfile, fieldnames=fields)
                    for row in reader:
                        if row['Name'] == str(ex_name):
                            res = 1    
                    if res == 0:
                        print("The Name you have entered is not exist...!")
            name = input("NAME : ")
            ph = int(input("PHONE NUMBER : "))
            mail = input("E-MAIL ID : ")
            update(ex_name,name,ph,mail)
            print("**********Conatact has been Updated**********")
        
        if ch == 3:
            while res == 0:
                name = input("Enter your existing name to DELETE : ")
                fields = ['Name', 'Phone Number', 'E-Mail ID']
                with open('Contact.csv', 'r') as csvfile:
                    reader = csv.DictReader(csvfile, fieldnames=fields)
                    for row in reader:
                        if row['Name'] == str(name):
                            res = 1    
                    if res == 0:
                        print("The Name you have entered is not exist...!")
            delete(name)
            print("**********Contact has been Deleted**********")
        
        if ch == 4:
            while res == 0:
                name = input("Enter your existing name to VIEW : ")
                fields = ['Name', 'Phone Number', 'E-Mail ID']
                with open('Contact.csv', 'r') as csvfile:
                    reader = csv.DictReader(csvfile, fieldnames=fields)
                    for row in reader:
                        if row['Name'] == str(name):
                            res = 1    
                    if res == 0:
                        print("The Name you have entered is not exist...!")
            view(name)

        if ch == 5:
            print("All Changes are Saved...!")
            print("**********EXITING**********")
            i = 1

        if ch not in [1,2,3,4,5]:
            print("You have entered the wrong choice...!")

        res = 0
    except :
        print("You have Entered the Wrong Choice...!")
