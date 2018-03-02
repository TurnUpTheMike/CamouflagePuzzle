from wordbank.wordbank import WordBank
from abc import ABC, abstractmethod


class WordBankGeneratorBase(ABC):
    def __init__(self, app_properties):
        self.properties = app_properties

    @abstractmethod
    def generate_word_bank(self):
        pass


class WordBankGeneratorHardCoded(WordBankGeneratorBase):
    def __init__(self, app_properties):
        super().__init__(app_properties)

    def generate_word_bank(self):
        bank = WordBank(app_properties=self.properties)
        bank.hash_by_letter = {
            'a': ['banana'],
            'b': ['bubble'],
            'c': ['practice'],
            'd': ['candle'],
            'e': ['treacherous'],
            'f': ['perfect'],
            'g': ['laugh'],
            'h': ['beach'],
            'i': ['guitar'],
            'j': ['trajectory'],
            'k': ['blanket'],
            'l': ['color'],
            'm': ['smile'],
            'n': ['stamina'],
            'o': ['blood'],
            'p': ['partner'],
            'r': ['quilt'],
            'q': ['morning'],
            's': ['respect'],
            't': ['flatten'],
            'u': ['hundred'],
            'v': ['alive'],
            'w': ['below'],
            'x': ['expert'],
            'y': ['player'],
            'z': ['zebra']
        }
        return bank
