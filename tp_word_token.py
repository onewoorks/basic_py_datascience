import nltk

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_token = nltk.word_tokenize(word_data)
print(nltk_token)

sentences_data = "Sun rises in the east. Sun sets in the west."
nltk_token = nltk.sent_tokenize(sentences_data)
print("\n")
print(nltk_token)