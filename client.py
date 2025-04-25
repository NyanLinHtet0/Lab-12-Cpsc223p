import json

#TODOS: add error checking
#TODOS: check duplicate entries and reject them


class Client():
    #class variable dictionary to store accounts in runtime
    account_data = {}
    def __init__(self, name, password):
        self.__name = name
        self.__password = password
        Client.account_data[name]=password
        
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