def draw_letters():

    import random

    main_letters_list = ["a", "a", "a", "a", "a", "a", "a", "a","a", "b", "b", "c", "c", "d", "d", "d", "d", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "f", "f", "g", "g", "g", "h", "h", "i", "i", "i", "i", "i", "i", "i", "i", "i", "j", "k", "l", "l", "l", "l", "m", "m", "n", "n", "n", "n", "n", "n", "o", "o", "o", "o", "o", "o", "o", "o", "p", "p", "q", "r", "r", "r", "r", "r", "r", "s", "s", "s", "s", "t", "t", "t", "t", "t", "t", "u", "u", "u", "u", "v", "v", "w", "w", "x", "y", "y", "z"]  

    main_letters_list_copy = []
    user_hand = []


    for letter in main_letters_list:
        main_letters_list_copy.append(letter)

    x = 0
    while x < 10:
        letter = random.choice(main_letters_list_copy)
        user_hand.append(letter.capitalize())
        main_letters_list_copy.remove(letter)
        x += 1

    return user_hand

def uses_available_letters(word, letter_bank):


    letter_bank_copy = []
    for letter in letter_bank:
        letter_bank_copy.append(letter)
    
    for letter in word:
        if letter not in letter_bank_copy:
            return False
        elif letter in letter_bank_copy:
            letter_bank_copy.remove(letter)

    return True
    

def score_word(word):
    score_chart = { 
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], 
        2: ["D", "G"], 
        3: [ "B", "C", "M", "P"], 
        4: ["F", "H", "V", "W", "Y"], 
        5: ["K"], 
        8 : ["J", "X"], 
        10: [ "Q", "Z"] 
        }
    word = word.upper()
    score = 0
    for letter in word:
        for key, value in score_chart.items():
            if letter in value:
                score += key
    
    if len(word) >= 7:
        score += 8

    return score
   

def get_highest_word_score(word_list):
    pass