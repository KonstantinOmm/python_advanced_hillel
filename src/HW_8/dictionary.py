big_string: str = " The first second was alright, but the second second was tough."

words: list = big_string.split()
often_words: set = set(words)
occurring_words: dict = dict()

for word in often_words:
    occurring_words[word] = words.count(word)

print(sorted([(count, word) for word, count in occurring_words.items()]).pop()[1])
