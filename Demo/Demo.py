import sys

from soupsieve import select

sys.path.insert(0, 'BruteForce')
sys.path.insert(1, 'Dictionary')
sys.path.insert(2, 'BadBruteForce')

import hashlib
import time
from Dictionary import DictionaryAttackUser
from BruteForce import BruteForceUserAttack
from BadBruteForce import BadUserAttack

DatabaseFile = 'Demo/Database.txt'

def Banner():
    BannerFile = open('Demo/Banner.txt', 'r')
    Banner = BannerFile.read()
    print(Banner)

def SearchUsername(Username):
    with open(DatabaseFile,"r") as Database:
        for line in Database.readlines():
            if Username in line:
                return True
        
        return False

def Bruteforce(Username):
    try:
        if SearchUsername(Username) == True:
            print(f"[*] Username {Username} Found...")
            print("[*] Running Dictionary Attack...")

            print("==========\n[ STATUS ]: Started...\n==========")
            start = time.time() # begin timer
            
            BruteForceUserAttack(Username)

            print("==========\n[ STATUS ]: Done...\n==========")
            end = time.time()
            print("Completed in: ",end - start, "s")

        else:
            print(f"Username {Username} Not Found, Please Try Again...")
            print("Please select a username to search in the json Database.")
            Userin = input("Username: ")
            Bruteforce(Userin)

    except FileNotFoundError:
        print("Database File has not been created, please create one and retry the demo...")
        exit()

def Dictionary(Username):
    try:
        DictFile = LoadDictionary()
        if SearchUsername(Username) == True:
            print(f"[*] Username {Username} Found...")
            print("[*] Running Dictionary Attack...")
            print("==========\n[ STATUS ]: Started...\n==========")
            start = time.time() # begin timer

            DictionaryAttackUser(Username, DictFile)

            print("==========\n[ STATUS ]: Done...\n==========")
            end = time.time()
            print("Completed in: ",end - start,"s")

        else:
            print(f"Username {Username} Not Found, Please Try Again...")
            print("Please select a username to search in the json Database.")
            Userin = input("Username: ")
            Dictionary(Userin)

    except FileNotFoundError:
        print("Database File has not been created, please create one and retry the demo...")
        exit()

def Bad(Username):
    if SearchUsername(Username) == True:
        print(f"[*] Username {Username} Found...")
        print("[*] Running Dictionary Attack...")
        print("==========\n[ STATUS ]: Started...\n==========")
        start = time.time() # begin timer

        BadUserAttack(Username)

        print("==========\n[ STATUS ]: Done...\n==========")
        end = time.time()
        print("Completed in: ",end - start,"s")

    else:
        print(f"Username {Username} Not Found, Please Try Again...")
        print("Please select a username to search in the json Database.")
        Userin = input("Username: ")
        Bad(Userin)

def LoadDictionary():
    Userin = input("Do you have a Dictionary file you'd like to run? (Y/N): ")
    if Userin.lower() == "y" or Userin.lower() == "yes":
        Userin = input("Enter File Path: ")
        DictionaryFile = Userin
    elif Userin.lower() == "n" or Userin.lower() == "no":
        DictionaryFile = "Dictionary/Dictionary.txt"
    else:
        print("Please Try Again...")
        LoadDictionary()
    
    return DictionaryFile;

def SelectAttacks():
    print("===\nSELECT AN OPTION FROM BELOW\n===\n1 > Bruteforce\n2 > Dictionary\n3 > Surprise Me!\n4 > Exit")
    Userin = input("Enter: ")
    if Userin == "1":
        print("Please select a username to search in the json Database.")
        Userin = input("Username: ")
        Bruteforce(Userin)

    elif Userin == "2":
        print("Please select a username to search in the json Database.")
        Userin = input("Username: ")
        Dictionary(Userin)

    elif Userin == "3":
        print("Are you sure? (Y/N): ")
        Userin = input("Enter: ")
        if Userin.lower() == "y" or Userin.lower() == "yes":
            print("Okay...")
            Userin = input("Username: ")
            Bad(Userin)
        
        elif Userin.lower() == "n" or Userin.lower() == "no":
            print("Good Choice...")
            SelectAttacks()
        
        else:
            print("Didn't quite understand that...")
            SelectAttacks()
            
    elif Userin == "4":
        print("Goodbye!")
        exit()
    else:
        print("Please Try Again...")

def PromptForStuff():
    Userin = input("Would you like to add users to the Json Database for the demo? (Y/N/Q): ")
    if Userin.lower() == "y" or Userin.lower() == "yes":
        Username = input("Enter Username: ")
        Password = input("Enter Password: ")

        PasswordHashed = hashlib.sha256(Password.encode('utf-8')).hexdigest()

        with open(DatabaseFile,"a") as Database:
            if SearchUsername(Username) == False:
                Database.write(Username+":"+PasswordHashed+'\n')
                print("User Added...")
            else:
                print("[!] Username Collision, please try another username...")
                PromptForStuff()
                

        PromptForStuff()

    elif Userin.lower() == "n" or Userin.lower() == "no":
        SelectAttacks()

    elif Userin.lower() == "q" or Userin.lower() == "exit":
        print("Goodbye!")
        exit()

    else:
        print("Please Try Again...")
        PromptForStuff()

def Driver():
    Banner()
    PromptForStuff()

Driver()