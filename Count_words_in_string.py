#Counting words in a string

is_looping = True						#Just keep looping. Just keep looping.

while is_looping == True:				#Keeps this looping until 'exit' is typed.
	word_count = 0							#Variable definitions
	list_sentence = []
	last_char_isalnum = False
	
	sentence = raw_input("\nPlease type sentence to be analyzed below, or type 'exit' to quit.\nInput: ")#Tells user to type something
	list_sentence = list(sentence) 	#Converts the sentence to a list for easier analysis.
	sentence = sentence.lower()			#Converts to lowercase, aids checking for 'exit'.
	if sentence == "":
		print "No input was detected."	#User did not input anything.
	elif sentence == "exit":
		is_looping = False				#User want to exit.
	else:								#User typed something. Analyze!
		for every_character in range(len(list_sentence)):
			if list_sentence[every_character].isalnum() == True\
					and last_char_isalnum == False:
				#If character is an alphanumerical and last character was not (I.e: A new word in the count)
				word_count += 1
				last_char_isalnum = True
			elif list_sentence[every_character].isalnum() == True\
					and last_char_isalnum == True:
				#If character is alphanumerical and last character was as well (I.e: continuation of a word)
				pass
			else:
				#Character is not an alphanumerical but last character was one (I.e: End of a word)
				last_char_isalnum = False

		if word_count == 1:
			print "There is one word in the sentence provided."
		else:
			print "There are %i words in the sentence provided" % (word_count)