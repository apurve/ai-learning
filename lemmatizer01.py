from nltk import WordNetLemmatizer, download


if __name__ == "__main__":
    download('wordnet')
    words = ["running", "ran", "easily", "fairly", "better", "best", "happily", "happier", "happiest", "go", "gone", "going"]
    lemmatizer = WordNetLemmatizer()
    
    print("Lemmatizer Results:")
    for word in words:
        print(f"{word} | ---> | {lemmatizer.lemmatize(word, pos='v')}")  # 'v' for verb, can be adjusted for other parts of speech