def spin_words(sentence):
    final_word_string = []  # Make list for final sentence
    words = sentence.split()  # Turn sentence into list of words
    print("The list of words is: " + str(words))
    
    for word in words:  # Go through each word
        if word == ":":
            print("Something cool happened")
        if len(word) > 5:  # If word is longer than 5 characters
            selected_word = list(word)  # Turn word into list of characters
            selected_word.reverse()  # Reverse the list of characters
            selected_word = "".join(selected_word)  # Join the reversed list into a string
            final_word_string.append(selected_word)  # Add reversed word to final list
        else:
            final_word_string.append(word)  # Add word to final list as is

#   RETURN / PRINT (" ".join(final_word_string))  # Join the list of words into a final sentence and return


spin_words("Spaces in spaces Strings Just but in of letters more takes Spaces included': 'secapS in secaps sgnirtS Just but in of srettel more takes secapS dedulcni' should equal 'secapS in secaps sgnirtS Just but in of srettel more sekat secapS dedulcni")