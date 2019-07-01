import nltk
from nltk.stem import WordNetLemmatizer

wordnet_lemmitizer = WordNetLemmatizer()

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_token = nltk.word_tokenize(word_data)

for w in nltk_token:
    print("Actual: {} Stem: {}".format(w, wordnet_lemmitizer.lemmatize(w)))