from nltk import download
from nltk.tokenize import word_tokenize, sent_tokenize

if __name__ == "__main__":
    corpus = """The quick brown fox jumps over the lazy dog.  
                Hello, world! This is a test sentence.
                NLTK is a powerful library for text processing."""
    
    download('punkt_tab')
    sentences = sent_tokenize(corpus)

    for sentence in sentences:
        print("Sentence:", word_tokenize(sentence))

    print("*****VS*****")

    print("Words:", word_tokenize(corpus))