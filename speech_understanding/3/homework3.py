def cancellation(input_list, stop_word):
	result = []
	for word in input_list:
		if word == stop_word:
			break
		result.append(word)
	return result


def copy_all_but_skip_word(input_list, skip_word):
	return [word for word in input_list if word != skip_word]


def list_to_dict(input_list):
	return {index: value for index, value in enumerate(input_list)}


def my_average(input_list):
	return sum(input_list) / len(input_list)