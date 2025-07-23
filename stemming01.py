from nltk import PorterStemmer, RegexpStemmer

if __name__ == "__main__":
    words = ["running", "ran", "easily", "fairly", "better", "best", "happily", "happier", "happiest"]
    stemmer = PorterStemmer()
    print("Porter Stemmer Results:")
    for word in words:
        print(f"{word} | ---> | {stemmer.stem(word)}")

    print("\n*****VS*****\n")

    print("Regex Stemmer Results:")
    regex_stemmer = RegexpStemmer("ing$|ly$|er$", min=2)
    for word in words:
        print(f"{word} | ---> | {regex_stemmer.stem(word)}")