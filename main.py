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
message_menu = ["Message", "View Inbox","logout"]

#Read existing data to load last state
acc_manager.read_all()

#start the menu
choice = menu(main_menu)

while(choice!= 4):
    #Login
    if(choice == 1):
        name = input("Username: ")
        pw = input("Password: ")
        logged_status = acc_manager.login(name,pw)
        if  logged_status == True:#login comparison
            logged_in_menu = menu(message_menu,False)
            while(logged_in_menu != 3):
                #send message function
                if(logged_in_menu == 1):
                    destination = input("who do you want to message?: ")
                    message = input("what is the message you would like to send: ")
                    acc_manager.print_all()
                    acc_manager.send_message(name,message,destination)
                elif(logged_in_menu == 2):
                    messages = acc_manager.view_inbox(name)
                    for person in messages:
                        print(person)
                        for message in messages[person]:
                            # print(message)
                            print(f'  {message['message']}({message['time']})')
                        print()     
                logged_in_menu = menu(message_menu,False)
        else:
            print("Wrong login information")
            break
            
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

    choice = menu(main_menu,False)
    
    





