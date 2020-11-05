import unittest
import word_processor

class Words(unittest.TestCase):

    def test_convert_list(self):
        words = word_processor.convert_to_word_list(
            'My name is Marc, is Zee a loser ?')
        self.assertEqual(['my','name','is','marc','is','zee','a','loser'],words)
    def test_words_longer(self):
        words = word_processor.words_longer_than(3,
            'My name is Marc, is Zee a loser ?')
        self.assertEqual(['name','marc','loser'],words)
    def test_lengths(self):
        words = word_processor.words_lengths_map(
            'My name is Marc, is Zee a loser ?')
        self.assertEqual({1: 1, 2: 3, 3: 1, 4: 2, 5: 1},words)
    def test_count(self):
        words = word_processor.letters_count_map(
            'My name is Marc, is; Zee a loser ?')
        self.assertEqual({'a': 3, 'b': 0, 'c': 1, 'd': 0, 'e': 4, 'f': 0, 
                          'g': 0, 'h': 0, 'i': 2, 'j': 0, 'k': 0, 'l': 1, 'm': 3, 
                          'n': 1, 'o': 1, 'p': 0, 'q': 0, 'r': 2, 's': 3, 't': 0, 
                          'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 1, 'z': 1},words)
    def test_most_char(self):
        words = word_processor.most_used_character(
            'My name is Marc, is; Zee a loser ?')
        self.assertEqual('e',words)
        pass
    
    
if __name__ == "__main__":
    unittest.main()