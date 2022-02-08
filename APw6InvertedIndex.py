import copy
import json


class InvertedIndex:
    def __init__(self, word_to_docs_mapping):
        self.words_dict = copy.deepcopy(word_to_docs_mapping)

    def query(self, words):
        word_intersection = set()
        first_word = True

        for word in words:
            if first_word:
                word_intersection = self.words_dict[word]
                first_word = False
            else:
                word_intersection &= self.words_dict[word]
        return word_intersection

    def dump(self, filepath):
        with open(filepath, 'w') as f:
            f.truncate()
            json.dump(self.words_dict, f,
                      default=lambda x: list(x) if isinstance(x, set) else x)

    @classmethod
    def load(cls, filepath):
        with open(filepath, 'r') as f:
            xi = json.load(f)
            ii_restored = {
                key: set(value)
                for key, value in xi.items()
            }
        return InvertedIndex(ii_restored)


def load_document(filepath):
    wiki_dict = dict()

    with open(filepath, mode="r", encoding="utf-8") as f:
        for line in f:
            text_id, text = line.split('\t', maxsplit=1)
            key = int(text_id)
            value = text.rstrip().lstrip()
            wiki_dict[key] = value

    return wiki_dict


def build_inverted_index(articles):
    word_dict = dict()

    for text_id, text in articles.items():
        words = text.split()
        for word in words:
            if word_dict.get(word, None) is None:
                word_dict[word] = set()
            word_dict[word].add(text_id)

    return InvertedIndex(word_dict)

d = load_document('wikipedia_sample.txt')
ii = build_inverted_index(d)
print(sorted(ii.query(['company'])))
print(sorted(ii.query(['regarded'])))
print(sorted(ii.query(['Each'])))
print(sorted(ii.query(['rise'])))
print(' ')
print(sorted(ii.query(['regarded', 'Each', 'company', 'rise'])))