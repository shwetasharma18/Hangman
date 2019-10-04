import string
import random

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    
    my_file = open("words.txt")
    words = my_file.read()
    words_list = words.split(" ")
    return (words_list)
    my_file.close()

load_words()

def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    word_list = load_words()
    random_word = random.choice(word_list)
    secret_word = random_word.lower()
    return (secret_word)

choose_word()
