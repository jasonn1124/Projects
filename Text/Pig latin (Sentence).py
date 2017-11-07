#Text - Pig latin (Sentence)

#Current solution was is to add 'ay' to the end of each word, shift the first letter back, then add the '-'.
#Further reading has revealed that pig latin is not as simple as it looks.
#Both consonants and consonant clusters at the start of words are shifted back.
#Vowels are not shifted back, and -ay is just appended to the end.
#This can be resolved by simply comparing the first letter to a list of consonants and vowels to see which one it matches.
#Consonant clusters can be detected by removing everything up to the first vowel.
#This is more complicated and I can't be arsed to do it because screw pig latin.


sentence = raw_input("Type something: ")
if sentence == "":
	print "Nothing was typed."
else:
	list_sentence = list(sentence)	#Converts to list

is_looping = True
word_start_index = 0
word_end_index = 0
previous_isalnum = False
counter = 0

while is_looping == True:
	if counter > len(list_sentence):
		is_looping = False
		print "".join(list_sentence)
	elif counter == len(list_sentence) or\
	list_sentence[counter].isalnum() == False and\
	previous_isalnum == True:	#End of a word
		word_end_index = counter
		list_sentence.insert(word_end_index, "y")
		list_sentence.insert(word_end_index, "a")
		list_sentence.insert((word_end_index-1), list_sentence.pop(word_start_index))
		list_sentence.insert((word_end_index-1), "-")
		previous_isalnum = False
		counter += 4
	elif list_sentence[counter].isalnum() == True and\
	previous_isalnum == False:	#Start of a word
		word_start_index = counter
		previous_isalnum = True
		counter += 1
	elif list_sentence[counter].isalnum() == True and\
	previous_isalnum == True:	#Cont of a word
		counter += 1
