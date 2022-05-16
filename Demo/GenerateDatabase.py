import json

def PromptForStuff():
    Userin = input("Would you like to create a Json Database for the demo? (Y/N): ")
    if Userin.lower() == "y" or Userin.lower() == "yes":
        with open("Demo/Database.json","r+") as Database:
            DB = json.load(Database)
            Username = input("Enter Username: ")
            Password = input("Enter Password: ")

            Data = {
                Username: Password
            }
            
            DB.append(Data)
            DB.seek(0)
            json.dump(DB, Database, indent=1)

    elif Userin.lower() == "n" or Userin.lower() == "no":
        print("Goodbye!")
        exit()

PromptForStuff()

        
