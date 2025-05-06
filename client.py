import json

#TODOS: add error checking
#TODOS: check duplicate entries and reject them


class Client():
    #class variable dictionary to store accounts in runtime
    
    def __init__(self):
        self.account_data = {}
    
    def add_account(self, name, pw):
        #check existing account first
        #add if it doesn't exist, add to dictionary
        #if it does exist, error account already exists
        self.account_data[name] = pw
        
    def delete_account(self,name):
        if(name in self.account_data):
            pw = input("Enter password to delete account: ")
            if pw == self.account_data[name]:
                del self.account_data[name]
        else:
            print(f"Account '{name}' deleted.")
            print(f"Account '{name}' does not exist.")

    def change_password(self, name, pw, new_pw):
        #change password if the pw match with old pw
        if pw == self.account_data.get(name):
            self.account_data[name] = new_pw
        else:
            raise ValueError("Incorrect Password")
        
    #class method to save all account names
    def save_all(filename="account_management.json"):
        with open(filename, "w") as f:
            json.dump(Client.account_data, f, indent=4)
    
    #class method to read all accounts from json to runtime
    def read_all(self, filename="account_management.json"):
        with open(filename, "r") as f:
            self.account_data = json.load(f)

    def login(self, name, pw):
        if name in self.account_data:
            if self.account_data[name] == pw:
                return True
        else:
            return False
        
    def send_message(self, name, source, destination):
        if destination in self.account_data:
            message_data ={
                "from": source,
                "to": destination,
                "message": f"Message from {name}"
            }
            #Load existing messages or intialize empty list
            try:
                with open("message_log.txt", "r") as f:
                    messages = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                messages = []
            # Append new message
            messages.append(message_data)
            
            #Write updated list back to file
            with open("message_log.txt", "w") as f:
                json.dump(messages, f, indent=4)
        else:
            return False
        
    def print_all(self):
        print(self.account_data)
            

            


