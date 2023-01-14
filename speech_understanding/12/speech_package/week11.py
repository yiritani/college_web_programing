import speech_recognition as sr


def recognize_microphone():
    speech = sr.Recognizer()
    while True:
        print('Python is listening...')
        with sr.Microphone() as source:
            speech.adjust_for_ambient_noise(source)
            try:
                audio = speech.listen(source)
                inp = speech.recognize_google(audio)
                break
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                continue
            except sr.WaitTimeoutError:
                continue
    return inp