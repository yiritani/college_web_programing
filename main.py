import nltk

import re

ignore_words = {
	'a',
	'an',
	'and',
	'as',
	'but',
	'for',
	'from',
	'nor',
	'of',
	'or',
	'so',
	'the',
	'to',
	'yet',
	'at',
	'by',
	'for',
	'from',
	'in',
	'into',
	'of',
	'off',
	'on',
	'onto',
	'out',
	'over',
	'to',
	'up',
	'with'
}
except_case = {'/', '-', ':'}

upper_case_part_of_speech = {'RB', 'RBR', 'RBS', 'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'VB', 'VBD', 'VBG', 'VBN',
							 'VBN', 'VBZ'}

song_title = 'Waking up to Coffee'.replace(
	'  ', ' ')
print('song_title', song_title)
separated_song_title = [i for i in re.split(r'([\(\) :-])', song_title) if i != '']
modified_song_title = ''
for index, word in enumerate(separated_song_title):
	target_word = word
	negative_target_compare_index = 1
	if separated_song_title[index - negative_target_compare_index] == ' ':
		negative_target_compare_index += 1
	try:
		if separated_song_title[index - negative_target_compare_index] in except_case:
			modified_song_title += word.capitalize()
		elif index != len(separated_song_title) - 1 and separated_song_title[index + 1] == ')':
			modified_song_title += word.capitalize()
		elif not target_word in ignore_words:
			modified_song_title += word.capitalize()
		elif target_word in ignore_words:
			modified_song_title += word.lower()
	except IndexError:
		pass

print('modified_song_title', modified_song_title)

morph = nltk.word_tokenize(modified_song_title)
print('morph', morph)
pos = nltk.pos_tag(morph)
print(pos)
for index, i in enumerate(pos):
	if i[1] in upper_case_part_of_speech:
		morph[index] = i[0].capitalize()

natural_language_processed_song_title = ' '.join(morph).replace('( ', '(').replace(' )', ')'). replace(' :', ':').replace(' - ', '-')
print('natural_language_processed_song_title', natural_language_processed_song_title)