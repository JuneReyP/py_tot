def count(text):
    words =text.split()
    word_frequencies = {}
    for word in words:
        word = word.lower().strip('.,!?;"\'()')
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1
    return word_frequencies