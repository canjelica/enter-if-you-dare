"""Given a phrase, return a dictionary with {<word length>: {<words>}}.

For example:

>>> word_lengths('cute cats chase fuzzy rats')
{4: {'cute', 'cats', 'rats'}, 5: {'chase', 'fuzzy'}}
Punctuation should be considered part of a word."""

#create dictionary to store results in string
#split string by space(turns into list)
#loop over each word in list, if length not in dictionary, add word at length
#if length in dictionary, add word

def find_word_lengths(sentence):
	"""Return dictionary of word lengths."""

	word_lengths = {}
	sentence = sentence.split(" ")
	for word in sentence:
		length = len(word)

		if length not in word_lengths:
			word_lengths[length] = {word}
		else:
			word_lengths[length].add(word)
	
	return word_lengths