import bs4
import speech_package


def extract_stories_from_NPR_text(webpage_text):
	'''
	Input:
	webpage_text (string): the text of a webpage

	Output:
	stories (list of strings): a list of the news stories in the web page
	'''
	soup = bs4.BeautifulSoup(webpage_text, "html.parser")
	stories = []
	for div_tag in soup.find_all('div', 'story-text'):
		title = div_tag.find('h3', 'title')
		teaser = div_tag.find('p', 'teaser')
		story = title.text + ". "
		if teaser:
			story += teaser.text
		stories.append(story)
	return stories


def read_nth_story(stories, n, filename):
	'''
	Input:
	stories (list of strings): a list of the news stories from a web page
	n (int): the index of the story you want me to read
	filename (str): filename in which to store the synthesized audio

	Output: None
	'''
	speech_package.synthesize(stories[n], "en", filename)
