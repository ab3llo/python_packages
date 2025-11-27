from collections import Counter
import re


def tokenize(text: str) -> list:
    """A small tokenizer returning word tokens from text.

    This is a minimal implementation to ensure the package works
    without external dependencies. It lowercases and extracts word
    characters.
    """
    if not text:
        return []
    return re.findall(r"\w+", text.lower())


class Document:
    def __init__(self, text: str = ""):
        self.text = text
        # pre tokenize the document with non-public tokenize method
        self.tokens = self._tokenize()
        # pre compute the document's word counts
        self.word_counts = self._count_words()

    def _tokenize(self):
        return tokenize(self.text)

    # non-public method to tally document's word counts with Counter
    def _count_words(self):
        return Counter(self.tokens)
