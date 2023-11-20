import re
from datetime import datetime

def get_year():
    '''Function to get curent year'''    

    return datetime.now().year


def is_strong_password(password):
    '''Function to check if password is strong enough'''
    
    # Regular expression pattern
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()-_+=])[A-Za-z\d!@#$%^&*()-_+=]{8,}$')
    
    # Check if the password matches the pattern
    if pattern.match(password):
        return True
    else:
        return False