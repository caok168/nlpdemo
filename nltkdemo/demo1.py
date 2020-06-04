import nltk

nltk.download()

sentence = """At eight o'clock on Thursday moring Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)

print(tokens)
