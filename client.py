import json

#TODOS: add error checking.

class Client():
    #class variable dictionary to store accounts in runtime
    data = {}
    def __init__(self, name, password):
        self.__name = name
        self.__password = password
        Client.data[name]=password
        
    #class method to save all account names
    def save_all(filename="account_management.json"):
        with open(filename, "w") as f:
            json.dump(Client.data, f, indent=4)
    
    #class method to read all accounts from json to runtime
    def read_all(filename="account_management.json"):
        with open(filename, "r") as f:
            Client.data = json.load(f)
        print(Client.data)  
            
    
Client("jack","pw123")        
Client("Jill","pw12345")
Client("Jill","pw12")
Client.save_all()
Client.read_all()