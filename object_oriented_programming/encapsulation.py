# encapsulation: wrapping variables and methods in one unit. e.g. in a class


class UserInfo:
    def __init__(self, username, email_address):
        self.username = username
        self.email_address = email_address

    def check_username(self, username_to_check):
        if username_to_check == self.username:
            return True
        else:
            return False
        
user = UserInfo('testuser', 'testuser@email.com')

print(user.check_username('testuser'))

print(user.check_username('user2'))