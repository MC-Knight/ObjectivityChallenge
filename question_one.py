import string

invalidcharacters= set(string.punctuation)

words = [word for word in input("Enter Text Here:").split(" ")]
cleared_words = []

for x in words:
    current_word = [i for i in x]
    for i in current_word:
        if i in invalidcharacters:
            current_word.remove(i)

    cleared_words.append("".join(current_word))

unique_words = set(cleared_words)
word_with_frequency = []


for i in unique_words:
    appeared = cleared_words.count(i)
    word_with_frequency.append([i, int(appeared)])


sorted_cleared_words_with_frequency = sorted(word_with_frequency, key=lambda x: -x[1])
print(sorted_cleared_words_with_frequency)


