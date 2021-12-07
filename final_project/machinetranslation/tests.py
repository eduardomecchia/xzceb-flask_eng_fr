import unittest
import translator

class TestEnglishToFrench(unittest.TestCase):
    def test_love(self):
        self.assertEqual(translator.english_to_french('Love'), 'Amour')

    def test_sun(self):
        self.assertEqual(translator.english_to_french('Sun'), 'Soleil')
    
    def test_null(self):
        self.assertRaises(ValueError, translator.english_to_french, None)
    
    def test_hello(self):
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
    
class TestFrenchToEnglish(unittest.TestCase):
    def test_love(self):
        self.assertEqual(translator.french_to_english('Amour'), 'Love')

    def test_sun(self):
        self.assertEqual(translator.french_to_english('Soleil'), 'Sun')
    
    def test_null(self):
        self.assertRaises(ValueError, translator.french_to_english, None)
    
    def test_hello(self):
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()