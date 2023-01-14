import bs4, speech_package, librosa


def read_nth_story(stories, n, filename):
	speech_package.synthesize(stories[n], "en", filename)


def extract_stories_from_NPR_text(webpage_text):
	'''
	Input:
	webpage_text (string): the text of a webpage

	Output:
	stories (list of strings): a list of the news stories in the web page
	'''
	try:
		stories = bs4.BeautifulSoup(webpage_text, "html.parser")
	except:
		raise RuntimeError('You need to write this part!')
	return stories


def synthesize_nth_story(stories, n):
	'''
	Input:
	stories (list of strings): a list of the news stories from a web page
	n (int): the index of the story you want me to read
	filename (str): filename in which to store the synthesized audio

	Output: None
	'''
	raise RuntimeError('You need to write this part!')
	return speech_wave, speech_rate
