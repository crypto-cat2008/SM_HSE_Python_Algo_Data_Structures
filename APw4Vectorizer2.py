import re


class CountVectorizer:
    def __init__(self, ngram_size):
        self.tokenSize = ngram_size
        self.tokenToIndex = dict()

    def fit(self, corpus):
        self.tokenToIndex = dict()
        tokens = set()
        for item in corpus:
            start = 0
            while len(item) - start >= self.tokenSize:
                tokens.add(item[start:start + self.tokenSize])
                start += 1
        self.tokenToIndex = {
            token: index
            for index, token in enumerate(sorted(tokens))
        }

    def transform(self, corpus):
        transformed_corpus = list()
        item_count = 0
        for item in corpus:
            transformed_corpus.append(list())
            for token in self.tokenToIndex:
                transformed_corpus[item_count].append(
                    len(re.findall('(?={0})'.format(token), item)))
            item_count += 1
        return transformed_corpus

    def fit_transform(self, corpus):
        self.fit(corpus)
        return self.transform(corpus)
