import speech_recognition as sr


def transcribe_wavefile(filename):
	'''
	Use sr.Recognizer.AudioFile(filename) as the source,
	recognize from that source,
	and return the recognized text.
	'''
	speech = sr.Recognizer()
	with sr.AudioFile(filename) as source:
		audio = speech.record(source)
		inp = speech.recognize_google(audio)
		print('The person in this audio file said:', inp, '.')
	# raise "You need to write this part!"
	return inp
