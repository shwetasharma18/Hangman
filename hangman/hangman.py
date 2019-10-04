import string
import words
from images import IMAGES

# End of helper code
# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
	if secret_word == get_guessed_word(secret_word, letters_guessed):
		return True
	else:
		return False    
'''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise
    '''
	
# Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess kar raha hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secret_word = "kindness", letters_guessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
    import string

    letters = string.ascii_lowercase
    letters_left = ""

    for letter in letters:
        
        if letter not in letters_guessed:

            letters_left += letter
    
    return letters_left


def hint(secret_word, letters_guessed):

    import random

    letters_not_guessed = []
    
    i = 0
    
    while i < len(secret_word):
        letter = secret_word[i]
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)
        i = i + 1

    return random.choice(letters_not_guessed)





def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Hangman game yeh start karta hai:

    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secret_word mei kitne letters hai

    * Har round mei user se ek letter guess karne ko bolte hai

    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi

    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai

    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secret_word)) + " letters long."
    print ""

    Difficulty_levels = raw_input("which level do you want to play :- Easy , Medium or Hard - " )
    
    total_lives = remaining_lives = 8

    images_index = [0,1,2,3,4,5,6,7]

    if Difficulty_levels not in ["easy", "medium", "hard"]:
        print "invalid choice, choose :- easy, medium or hard, we are moving ahead with the easy level"
    
    elif Difficulty_levels == "medium":
        total_lives = remaining_lives = 6
        images_index = [0,2,3,5,6,7]
    
    elif Difficulty_levels == "hard":
        total_lives = remaining_lives = 4
        images_index = [1,3,5,7]
    
    letters_guessed = []
            
    
    checking = 0
        
    while True:
    
    	available_letters = get_available_letters(letters_guessed)
    	print "Available letters: " + available_letters

    	guess = raw_input("Please guess a letter: ")
        letter = guess.lower()
        
        if checking >= 3:
                print "Sorry no more hints available"

        if checking < 3:
            if guess == "hint":
                checking += 1
                letter = hint(secret_word, letters_guessed)

        if letter.isalpha()== True:
            if letter in secret_word:
                letters_guessed.append(letter)
                print "Good guess: " + get_guessed_word(secret_word, letters_guessed)
            
                print ""
                if is_word_guessed(secret_word, letters_guessed) == True:
                    print " * * Congratulations, you won! * * "
                    print ""
                    break
            
            else:
                print "Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
                
                
                if remaining_lives == 0:
                    print "no more lives :("
                    print "Sorry you lost the game :("
                    break
                
                print IMAGES[images_index[total_lives-remaining_lives]]
                
                print "you have remaining lives" + " - " , remaining_lives
                
                print ""
               
                letters_guessed.append(letter) 
                
                remaining_lives -= 1	
        else:
            print "invalid input"

# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program

word_list = words.choose_word()
hangman(word_list)
