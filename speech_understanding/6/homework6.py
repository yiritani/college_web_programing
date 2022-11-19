import numpy as np
import librosa
import librosa.feature

'''
homework6.py

Copy this text to a new text file, and then edit it
so that the functions below perform the tasks specified.
'''


def waveform_to_cstft(speech_wave, hop, win):
	'''
	Given a speech_wave, this function should return a CSTFT
	(a complex-valued short-time Fourier transform)
	with the specified hop_length and win_length.
	'''
	cstft = librosa.stft(speech_wave, hop_length=hop, win_length=win)  # CHANGE THIS!
	return cstft


def cstft_to_mstft(cstft):
	'''
	Given a CSTFT, this function should return an MSTFT
	(a magnitude short-time Fourier transform).
	'''
	hop = int(0.010 * 1)
	win = int(0.025 * 1)

	mstft = np.abs(cstft)  # CHANGE THIS!
	return mstft


def mstft_to_sgram(mstft):
	'''
	Given an MSTFT (a magnitude short-time Fourier transform),
	this function should return a spectrogram.
	'''
	sgram = np.log(mstft)  # CHANGE THIS!
	return sgram


def waveform_to_mmgram(speech_wave, speech_rate, hop, win):
	'''
	Given a speech_wave, this function should return an MMGRAM
	(a magnitude mel-spectrogram)
	with the specified speech_rate, hop_length, and win_length,
	and with n_mels=40, and fmax=16000.
	'''
	mmgram = librosa.feature.melspectrogram(y=speech_wave,
											sr=speech_rate,
											hop_length=hop,
											win_length=win,
											n_mels=40,
											fmax=16000)
	return mmgram


def mmgram_to_melgram(mmgram):
	'''
	Given an MMGRAM (a magnitude mel-spectrogram),
	this function should return a mel-spectrogram.
	'''
	melgram = np.log(mmgram)  # CHANGE THIS!
	return melgram


def melgram_to_melspectrum(melgram):
	'''
	Given a mel-spectrogram, return a mel-spectrum.
	'''
	melspectrum = np.average(
		melgram,
		axis=1
	)
	return melspectrum


def melspectrum_to_zmms(melspectrum):
	'''
	Given a mel-spectrum, return a ZMMS
	(a zero-mean mel-spectrum).
	'''
	average = np.average(melspectrum)
	zmms = melspectrum - average
	return zmms


def recognize_speech(test_speech, models, labels):
	'''
	Given a test_speech, a list of 3 models, and a list of 3 labels,
	return a list of three distances, and the best label.
	'''

	# The three distances are all zero until we compute them
	distances = [0, 0, 0]

	# Compute the distances
	for i in range(3):
		distances[i] = np.linalg.norm(test_speech - models[i])

	# Find out which one was best
	best_label = labels[np.argmin(distances)]

	return distances, best_label
