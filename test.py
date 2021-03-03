from string import ascii_lowercase

letters_guessed=["a","r","z","q","u","n"]
word="queen"

# --------------------------------------------------------------------------------------
def get_remaining_letters (letters_guessed):

# This list of alphabets is coming from internal python function
  list_of_alphabets = list(ascii_lowercase)
# Final list if the one that will be returned as a string
  final_list_of_alphabets =[]
  final_string_of_alphabets=""

  for current_alpha in list_of_alphabets:
    current_alpha_is_present=False
    for current_guess_alpha in letters_guessed:
        if(current_alpha==current_guess_alpha):
            current_alpha_is_present=True
    if(current_alpha_is_present ==False):
        final_list_of_alphabets.append(current_alpha)
    
  return final_string_of_alphabets.join(final_list_of_alphabets)
        




# --------------------------------------------------------------------------------------
# in this one take letters from word one by one and check in guessed letters.
def is_word_guessed(word,letters_guessed):
    list_of_word = list(word)
    print(list_of_word)
    total_matching_words=0

    for current_word_alphabet in list_of_word:
        for current_guessed_alphabet in letters_guessed:
            if(current_word_alphabet==current_guessed_alphabet):
                total_matching_words+=1

# If the number of matching words is equal to the length of the word then it means all words are present, otherwise not.
    if(total_matching_words==len(list_of_word)):
        print("All is good you win")    
        return True
    else:
        print("Word is not guessed yet")  
        return False   









# --------------------------------------------------------------------------------------

def get_guessed_word(word,letters_guessed):
    list_of_word=list(word)
    final_word_to_display_list=[]
    final_word_to_display_string=""

    for current_word_alphabet in list_of_word:
        word_is_present=False
        for current_guessed_alphabet in letters_guessed:
            if(current_word_alphabet==current_guessed_alphabet):
                word_is_present=True
        if(word_is_present):
            final_word_to_display_list.append(current_word_alphabet)  
        else:
            final_word_to_display_list.append("_ ")   

    # print( final_word_to_display_string.join(final_word_to_display_list))

    return final_word_to_display_string.join(final_word_to_display_list)






remaining_letters = get_remaining_letters (letters_guessed)
word_guessed=is_word_guessed(word,letters_guessed)
progress=get_guessed_word(word,letters_guessed)
# print(word_guessed)
print(progress)
# print(remaining_letters)