class SentenceReader(object):
    def __init__(self, path, func=None):
        self.path = path
        self.func = func

    def __iter__(self):
        if self.func is None:
            with open(self.path, 'r') as f:
                for sentence in f:
                    yield sentence
        else:
            with open(self.path, 'r') as f:
                for sentence in f:
                    yield self.func(sentence)