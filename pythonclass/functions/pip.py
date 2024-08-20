# # “Design a simple authentication system for a command-line application. 
# The system should allow users to register with a username and password,
#  and then log in using their credentials. Store the user credentials in 
#  a dictionary and ensure that passwords are checked securely without storing 
#  them in plain text in your code.”

from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)
class Authentication_system:
    def __init__(self):
        self.authentication = []
    def register(self,user_name,password):
        credentials = {"user_name":user_name,"password":password}
        encPassword = fernet.encrypt(password.encode())
        print("original string: ", password)
        print("encrypted string: ", encPassword)
        if credentials["password"].isalnum():
            self.authentication.append(credentials)
            return "You have registered successfully"
        else:
            return "Please input username and password again"
    def login(self,user_name,password):
        {"user_name":user_name,"password":password}
        encPassword = fernet.encrypt(password.encode())
        fernet.decrypt(encPassword).decode()
        for currentPassword in self.authentication:
            if currentPassword['password'] == password:
                 return "Login successful"
            else:
                return "Wrong username or password"
user = Authentication_system()
print(user.register("Mary","Mary123") )
print(user.login("Mary","Mary123"))