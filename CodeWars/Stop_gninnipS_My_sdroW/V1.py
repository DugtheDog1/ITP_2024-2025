
# THIS IS VERSION 1 and DID NOT WORK

# def spin_words(sentence):
#     current_word = []
#     final_sentence = []
#     final_reverse = []

#     if not sentence.endswith(" "):
#         sentence += " "



    
#     for x in sentence: #Go through the letters
#         if x == " ": #done with word
#             if len(current_word) >= 5: #Check the word length
#                 current_word.reverse() #Reverse
#                 final_reverse = ''.join(current_word)
#                 print(current_word)
#                 final_sentence.append(current_word) #APPEND NOT WORKING
#                 current_word.clear() 
#             else:
#                 # new_word = ''.join(current_word) #If not join into string and print
#                 print(current_word)
#                 final_sentence.append(current_word) #APPEND NOT WORKING
#                 current_word.clear()
#         else:
#             current_word.append(x) #Add letter to the current_word list
#     print(final_sentence)
      
# spin_words("Hey fellow warriors")



