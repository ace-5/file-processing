from packages import utils
import unittest

line_for_n_gram = 'All men are mortal Socratis is a men Hence Socratis is mortal'

class TestUtilFuncs(unittest.TestCase):
    def test_read_csv(self):
        should_match = ['Vermont',
                        '',
                        'Virginia',
                        'Virginia',
                        'Colorado',
                        'New York',
                        'Idaho',
                        'Alabama',
                        'New Mexico',
                        'Pennsylvania']
        self.assertEqual(utils.read_csv('govt_urls_state_only.csv', 'Location')[:10], should_match, msg= "Please check if file exists in current directory")
    
    def test_remove_punctuation(self):
        word = "All men are mortal. Socratis is a men. Hence, Socratis is mortal"
        should_match = 'All men are mortal Socratis is a men Hence Socratis is mortal'
        self.assertEqual(utils.remove_punctuation(word), should_match)


  
class TestGenerateNgram(unittest.TestCase):
    def test_generate_1_gram(self):
        result_1gram = [['men'],
                        ['mortal'],
                        ['Socratis'],
                        ['men'],
                        ['Hence'],
                        ['Socratis'],
                        ['mortal']]
        self.assertListEqual(utils.generate_n_grams(line_for_n_gram, 1), result_1gram)
    
    def test_generate_2_gram(self):
        result_2gram = [['men', 'mortal'],
                        ['mortal', 'Socratis'],
                        ['Socratis', 'men'],
                        ['men', 'Hence'],
                        ['Hence', 'Socratis'],
                        ['Socratis', 'mortal']]
        self.assertListEqual(utils.generate_n_grams(line_for_n_gram, 2), result_2gram)
    
    def test_generate_3_gram(self):
        result_3gram = [['men', 'mortal', 'Socratis'],
                        ['mortal', 'Socratis', 'men'],
                        ['Socratis', 'men', 'Hence'],
                        ['men', 'Hence', 'Socratis'],
                        ['Hence', 'Socratis', 'mortal']]
        self.assertListEqual(utils.generate_n_grams(line_for_n_gram, 3), result_3gram)

