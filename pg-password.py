import random
import string

def load_wordlist(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

def generate_password(wordlist):
    password = random.choice(wordlist) + random.choice(string.digits + string.punctuation) + random.choice(string.punctuation + string.digits)
    return password

wordlist = load_wordlist('wordlist.txt')
print(generate_password(wordlist))