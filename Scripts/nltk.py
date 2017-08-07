from nltk.tokenize import sent_tokenize, word_tokenize

#tokenizing - form of grouping things - word tokenizers and sentence tokenizers

#corpora - body of text, ex: medical journal, presidential speeches, anything in the English language
#lexicon - words and their meanings

example_text = "Hello Mr. Smith, how are you doing today? The weather is great and python is awesome. The sky is pinkish blue. You should not eat cardboard."

print(sent_tokenize(example_text))

print(word_tokenize(example_text))
