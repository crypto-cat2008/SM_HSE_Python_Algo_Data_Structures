import copy
import json
import argparse


class InvertedIndex:
    def __init__(self, word_to_docs_mapping):
        self.words_dict = copy.deepcopy(word_to_docs_mapping)

    def query(self, words):
        word_intersection = set()
        first_word = True

        for word in words:
            if self.words_dict.get(word, None) is not None:
                result = self.words_dict[word]
            else:
                result = set()
            if first_word:
                word_intersection = copy.deepcopy(result)
                first_word = False
            else:
                word_intersection &= result

        return word_intersection

    def dump(self, filepath):
        with open(filepath, 'w') as f:
            f.truncate()
            json.dump(self.words_dict, f,
                      default=lambda x: list(x) if isinstance(x, set) else x)

    @classmethod
    def load(cls, filepath):
        with open(filepath, 'r', encoding="utf-8") as f:
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


def build(build_args):

    inverted_index1 = build_inverted_index(load_document(build_args.dataset))
    inverted_index1.dump(build_args.index)


def query(query_args):

    inverted_index2 = InvertedIndex.load(query_args.index)
    with open(query_args.query_file, mode="r", encoding="utf-8") as f_read:
        for line in f_read:
            words_to_check = line.split()
            results = inverted_index2.query(words_to_check)
            print(*sorted(results), sep=',')


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

command1_parser = subparsers.add_parser('build')
command1_parser.set_defaults(func=build)
command1_parser.add_argument('--dataset', dest='dataset')
command1_parser.add_argument('--index', dest='index')

command2_parser = subparsers.add_parser('query')
command2_parser.set_defaults(func=query)
command2_parser.add_argument('--index', dest='index')
command2_parser.add_argument('--query_file', dest='query_file')

args = parser.parse_args()
args.func(args)
