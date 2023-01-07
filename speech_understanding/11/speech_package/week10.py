import gtts


def synthesize(text, lang, filename):
	try:
		tts = gtts.gTTS(text=text, lang=lang)
		with open(filename, "wb") as f:
			tts.write_to_fp(f)

	except FileNotFoundError:
		raise RuntimeError("File not found. Please check the path and filename.")
