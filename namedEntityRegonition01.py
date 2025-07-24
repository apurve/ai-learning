import nltk
import numpy

if __name__ == "__main__":
    sentence="The Eiffel Tower was built from 1887 to 1889 by Gustave Eiffel, whose company specialized in building metal frameworks and structures."
    words=nltk.word_tokenize(sentence)

    nltk.download('averaged_perceptron_tagger')
    nltk.download('averaged_perceptron_tagger_eng')
    nltk.download('maxent_ne_chunker')
    nltk.download('words')
    nltk.download('maxent_ne_chunker_tab')
    # ...existing code...
    tag_elements=nltk.pos_tag(words)

    nltk.ne_chunk(tag_elements).draw()