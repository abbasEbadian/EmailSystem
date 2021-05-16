class MailServer:
    def __init__(self):
        self.users = []
        self.current_user = None
        self.main_menu()
    
    def register(self):
        email = input("Email: ")
        while email in [x.email for x in self.users]:
            email = input("Email already exists, try another one: ")
        while not email:
            email = input("Email: ")
        password = None
        while not password:
            password = input("Pasword: ")
        user = User(email, password)
        self.users.append(user)
        print("\n\n########")
        print("Account Created successfully !")
        print("########")
        self.main_menu()
    
    def login(self):
        broke = False
        email, password = None, None
        while not email:
            email = input("Email: ")
        while not password:
            password = input("Password: ")
        user = list(filter(lambda x: x.email == email and x.password == password, self.users))
        while not user :
            print("\nEmail or Password is wrong !\nTry again\n")
            print("type 'exit' to go back to main menu")
            email = input("Email: ")
            if email == 'exit':
                broke = True
                break
            password = input("Password: ")

            user = list(filter(lambda x: x.email == email and x.password == password, self.users))
        if broke:
            self.main_menu()
        else:
            user = list(user)[0]
            self.current_user = user
            self.user_menu(True)
    
    def get_user_by_email(self, email):
        user = filter(lambda x: x.email == email, self.users)
        return list(user) and list(user)[0] or None
    
    def change_password(self, user, new_pass):
        user.password = new_pass
        print("\n####\nPassword updated successfully!\n#### ")
    
    def send_new_email(self) :
        dest = input("Destination email: ")
        subject = input("Subject: ")
        body = input("body: ")
        email = Email(self.current_user, dest, subject, body)
        self.current_user.sent.append(email)
        dest_user = list(filter(lambda x: x.email == dest, self.users))
        if dest_user:
            dest_user[0].inbox.append(email)
        print("\n####\nEmail sent successfully !\n#### ")
    
    def view_inbox(self):
        if not self.current_user.get_inbox():
            print("###\nEmpty!!\n###")
        for i, email in enumerate(self.current_user.get_inbox()):
            print(f"{i+1}.")
            print("From: ", email.sender)
            print("Subject: ", email.subject)
            print("Body: ", email.text)
            print("------")
            
    def view_sent(self):
        if not self.current_user.get_sent_emails():
            print("###\nEmpty!!\n###")
        for i, email in enumerate(self.current_user.get_sent_emails()):
            print(f"{i+1}.")
            print("To: ", email.sender.email)
            print("Subject: ", email.subject)
            print("Body: ", email.text)
            print("------")
    
    def logout(self):
        self.current_user = None
        
    def main_menu(self):
        print("\n\nEnter command:")
        print("register --> Create new account")
        print("login --> Log in to your account")
        command = input(">")
        if command == "register":
            self.register()
        elif command == "login":
            self.login()
    
    def user_menu(self, init=False):
        if init:
            print("\n\nWelcome " +  self.current_user.email)
        print("Enter command:")
        print("send --> Send an email")
        print("inbox --> Show your inbox")
        print("sent --> Show your sent emails")
        print("logout --> Log out of account")
        command = input(">")
        if command == "send":
            self.send_new_email()
            self.user_menu()
        elif command == "inbox":
            self.view_inbox()
            self.user_menu()
        elif command == "sent":
            self.view_sent()
            self.user_menu()
        elif command == "logout":
            self.logout()
            self.main_menu()
        
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.inbox = []
        self.sent = []
    
    def get_inbox(self):
        return self.inbox
    
    def get_sent_emails(self):
        return self.sent
    
class Email:
    def __init__(self, sender, receiver, subject, text):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.text = text
        self.is_read = False
    
    def read(self):
        self.is_read = True
        
MailServer()       
