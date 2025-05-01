print("hello world")
print("hello world")
# Aijahlin

from client import Client

acc_manager = Client()
# acc_manager.add_account("jack","pw123")
# acc_manager.add_account("jill","pw123")
# acc_manager.add_account("John","pw123")
# acc_manager.delete_account("jill")
# acc_manager.print_all()

#this function is a menu function
def menu(lst):
    if 'Exit' in lst:
        pass
    else:
        lst.append('Exit')
    print()
    i = 1
    for item in lst:
        print(str(i) + '. ' + item)
        i += 1
    while True:
        try:
            choice = int(input('Input: '))
            if 1 <= choice <= len(lst):
                print()
                return choice
            else:
                print('Invalid choice. Please enter a number between 1 and', len(lst))
        except ValueError:
            print('Invalid input. Please enter a valid number.')
    
main_menu = ["Login", "Register"]
message_menu = ["Message", "logout"]
choice = menu(main_menu)
acc_manager.read_all()

while(choice!= 3):
    if(choice == 1):
        name = input("Username: ")
        pw = input("Password: ")
        if(acc_manager.login(name,pw) == True):#login comparison
            logged_in_menu = menu(message_menu)
            while(logged_in_menu != 3):
                destination = input("who do you want to message?: ")
                #check if user exists
                #if it does exists
                message = input("what is the message you would like to send: ")
                #send message Y or N
                confirmation = input("y/n")
                if confirmation == 'y':
                    acc_manager.message(name, message, destination)
                    #once y is pressed, we save to message.json/txt
                logged_in_menu = menu(message_menu)
        else:
            print("Wrong login information")





