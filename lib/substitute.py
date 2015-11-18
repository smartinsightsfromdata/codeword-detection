__author__ = 'linanqiu'


def generate_substitute_key(all_lines):
    from tfidf.word_rank_gamma import rank_words

    sorted_tfidf = rank_words(all_lines)

    num_substitute = 100

    selected_words = sorted_tfidf[:num_substitute]

    substitute_key = {}

    from random import shuffle

    selected_words_shuffled = list(selected_words)
    shuffle(selected_words_shuffled)

    # print selected_words
    # print selected_words_shuffled

    for original_word, substituted_word in zip(selected_words, selected_words_shuffled):
        substitute_key[original_word['word']] = substituted_word['word']

    return substitute_key


def generate_substitute_corpus(all_lines, substitute_key):
    all_lines_substituted = []

    for line in all_lines:
        new_line = []
        for word in line:
            if (word in substitute_key):
                new_line.append(substitute_key[word])
            else:
                new_line.append(word)

        all_lines_substituted.append(new_line)

    return all_lines_substituted
