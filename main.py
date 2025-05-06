print("hello world")
print("hello world")
# Aijahlin

from client import Client
from menu import menu
acc_manager = Client()
# acc_manager.add_account("jack","pw123")
# acc_manager.add_account("jill","pw123")
# acc_manager.add_account("John","pw123")
# acc_manager.delete_account("jill")
# acc_manager.print_all()

#menu constants    
main_menu = ["Login", "Register", "Delete Account"]
message_menu = ["Message", "logout"]

#Read existing data to load last state
acc_manager.read_all()

#start the menu
choice = menu(main_menu)

while(choice!= 4):
    #Login
    if(choice == 1):
        name = input("Username: ")
        pw = input("Password: ")
        if acc_manager.login(name,pw) == True:#login comparison
            logged_in_menu = menu(message_menu)
            while(logged_in_menu != 3):
                destination = input("who do you want to message?: ")
                message = input("what is the message you would like to send: ")
                acc_manager.print_all()
                acc_manager.send_message(name,message,destination)
                logged_in_menu = menu(message_menu)
        else:
            print("Wrong login information")
            
    #Register Account
    elif(choice == 2):
        name = input("Username: ")
        pw = input("Password:")
        acc_manager.add_account(name,pw)
    
    #Delete Account
    elif(choice == 3):
        name = input("Username: ")
        pw = input("Password:")
        acc_manager.delete_account(name,pw)
    





