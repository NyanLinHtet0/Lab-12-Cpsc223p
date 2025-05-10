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
TOTAL_WIDTH   = 80
RIGHT_MARGIN  = 15
CONTENT_WIDTH = TOTAL_WIDTH - RIGHT_MARGIN

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
                    print(f"messages on the right are sent messages\nmessages on the left are received messages")
                    for person in messages:
                        print(f"----------------{person}'s Chat------------------------------")
                        for message in messages[person]:
                            # print(message)
                            if message['from'] == person:
                                # right‑align into CONTENT_WIDTH columns
                                text = f"{message['message']}({message['time']})"
                                print(f"{text:<{CONTENT_WIDTH}}")
                            else:
                                # left‑align into CONTENT_WIDTH columns
                                text = f"({message['time']}){message['message']}"
                                print(f"{text:>{CONTENT_WIDTH}}") 

                logged_in_menu = menu(message_menu,False)
        else:
            print("Wrong login information")
            break
            
    #Register Account
    elif(choice == 2):
        name = input("Username: ")
        pw = input("Password:")
        if (acc_manager.add_account(name,pw)) == False:
            print(f"Account '{name}' already exists. TRY AGAIN with different username!\n")

    #Delete Account
    elif(choice == 3):
        name = input("Username: ")
        acc_manager.delete_account(name)

    choice = menu(main_menu,False)
    
    





