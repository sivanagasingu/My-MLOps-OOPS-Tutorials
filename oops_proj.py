class chatbook:
    def __init__(self):
        self.__name = "Default User"
        self.username = ''
        self.password = ''
        self.logged_in = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to chatbook! How would like to proceed?
                             1. Press 1 to Sign_Up 
                             2. Press 2 to Sign_In 
                             3. Press 3 to write a post
                             4. Press 4 to message a friend
                             5. Press any other key to Exit""")
        if user_input == '1':
            self.Sign_Up()
        elif user_input == '2':
            self.Sign_In()
        elif user_input == '3':
            self.write_post()
        elif user_input == '4':
            self.send_message()
        else:
            exit()


    def Sign_Up(self):
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        print("You have signed up successfully!!!")
        print("\n")
        self.menu()

    def Sign_In(self):
        if self.username== '' and self.password== '':
            print("Please signup first by pressing 1 in the main menu")
        else:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username == self.username and password == self.password:
                print("You have signed in successfully!!!")
                self.logged_in = True
            else:
                print("Please input correct credentials..")
            print("\n")
            self.menu()
            

    def write_post(self):
        if self.logged_in== True:
            txt = input("Enter your message here ....")
            print(f"Following content has been posted -> {txt}")    
        else:
            print("Please be sign-in before you post something")
            print("\n")
            self.menu()
        
    def send_message(self):
        if self.logged_in== True:
            txt = input("Enter your message here ....")
            friend = input("To whom you have to send a message... ")
            print(f"Your message has been sent to -> {friend}")    
        else:
            print("Please be sign-in before you sent a message to your {friend}")
            print("\n")
            self.menu()



user1 = chatbook()           