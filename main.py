print("Hello World!")
# print("hello world")
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
message_menu = ["Message", "View Inbox","Logout"]

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
                    while True:
                        destination = input("Who do you want to message?: ")
                        if destination in acc_manager.account_data:
                            message = input("What is the message you would like to send?: ")
                            acc_manager.send_message(name, message, destination)
                            break  # Exit retry loop after sending
                        else:
                            print(f"Destination '{destination}' does not exist. Please try again.")
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
    
    





