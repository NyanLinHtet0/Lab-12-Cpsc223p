import json

#TODOS: add error checking
#TODOS: check duplicate entries and reject them


class Client():
    #class variable dictionary to store accounts in runtime
    
    def __init__(self):
        account_data = {}
    
    def add_account(self, name, pw):
        #check existing account first
        #add if it doesn't exist, add to dictionary
        #if it does exist, error account already exists
        self.account_data.append({name:pw})
    
    def change_password(self, name, pw, new_pw):
        #change password if the pw match with old pw

        
    #class method to save all account names
    def save_all(filename="account_management.json"):
        with open(filename, "w") as f:
            json.dump(Client.account_data, f, indent=4)
    
    #class method to read all accounts from json to runtime
    def read_all(filename="account_management.json"):
        with open(filename, "r") as f:
            Client.account_data = json.load(f)
        print(Client.account_data)  
            
    
Client("jack","pw123")        
Client("Jill","pw12345")
Client("Jill","pw12")
Client.save_all()
Client.read_all()