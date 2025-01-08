import random

def load_wordlist(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

def generate_passphrase(num_words, wordlist):
    return '-'.join(random.choice(wordlist) for _ in range(num_words))

word_amount = int(input('Enter the number of words for the passphrase: '))
wordlist = load_wordlist('wordlist.txt')
passphrase = generate_passphrase(word_amount, wordlist)
print(passphrase)