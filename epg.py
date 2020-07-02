# 58110 words
from random import randint

word_list_file = "lowercase_english.txt"
# pick word randomly from list
def rand_word():
    """Picks word randomly from lowercase_english.txt word list"""
    with open(word_list_file) as word_list:
        word = word_list.readlines()[randint(0,58111)]
    return word

# pick word randomly 4 times and combine into passphrase
def passphrase():
    """Combines 4 words picked using rand_word() into a passphrase"""
    list = []
    for i in range(3):
    #pw = rand_word() + "-" + rand_word() + "-" + rand_word() + "-" + str(randint(999,10000))
        list.append(rand_word().rstrip())
    list.append(str(randint(999,10000)).rstrip())
    return "-".join(list)

print(passphrase())