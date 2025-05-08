def spin_words(sentence):
  sentence = sentence.split(' ')
  
  for words in sentence:
    if len(words) > 5:      
      ''.join(reversed(words))
    else:
      continue
  print(sentence)


spin_words("Hey fellow warriors" )

# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python


