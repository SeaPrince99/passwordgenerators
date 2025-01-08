import random
import string

def generate_password1(length):
    password = ''
    for i in range(length):
        password += random.choice(string.ascii_letters)
    return password


def generate_password2(length):
    if length < 7:
        return 'Password length should be at least 7 characters'
    password = ''
    for i in range(length):
        password += random.choice(string.ascii_letters)
    return password

def generate_password3(length):
    if length < 7:
        return 'Password length should be at least 7 characters'
    password = ''
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits)
    return password

def generate_password4(length):
    if length < 7:
        return 'Password length should be at least 7 characters'
    password = ''
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password

print(generate_password4(10))