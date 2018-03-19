from wordbank.wordbank import WordBank
from abc import ABC, abstractmethod


class WordBankGeneratorBase(ABC):
    def __init__(self, properties):
        self.properties = properties

    @abstractmethod
    def generate_word_bank(self):
        pass


class WordBankGeneratorHardCoded(WordBankGeneratorBase):
    def __init__(self, properties):
        super().__init__(properties)

    def generate_word_bank(self):
        bank = WordBank(properties=self.properties)
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
            'p': ['sample'],
            'r': ['partner'],
            'q': ['sequence'],
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
