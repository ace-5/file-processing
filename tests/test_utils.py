from packages import utils
import unittest

line_split = ['All',
                'men',
                'are',
                'mortal',
                'Socratis',
                'is',
                'a',
                'men',
                'Hence',
                'Socratis',
                'is',
                'mortal'
            ]

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
                        'Pennsylvania'
                    ]
        self.assertEqual(utils.read_csv('govt_urls_state_only.csv', 'Location')[:10], should_match, msg= "Please check if file exists in current directory")
    
    def test_remove_punctuation(self):
        word = "All men are mortal. Socratis is a men. Hence, Socratis is mortal"
        should_match = 'all men are mortal socratis is a men hence socratis is mortal'
        self.assertEqual(utils.remove_punctuation(word), should_match)
    
    def test_n_gram_freq(self):
        test_input = [['men'],
                        ['mortal'],
                        ['Socratis'],
                        ['men'],
                        ['Hence'],
                        ['Socratis'],
                        ['mortal']]
        result = [("['mortal']", 2), ("['men']", 2)]
        self.assertListEqual(utils.n_gram_freq(test_input, 2), result)


  
class TestGenerateNgram(unittest.TestCase):
    def test_generate_1_gram(self):
        result_1gram = [['men'],
                        ['mortal'],
                        ['Socratis'],
                        ['men'],
                        ['Hence'],
                        ['Socratis'],
                        ['mortal']]
        self.assertListEqual(utils.generate_n_grams(line_split, 1), result_1gram)
    
    def test_generate_2_gram(self):
        result_2gram = [['men', 'mortal'],
                        ['mortal', 'Socratis'],
                        ['Socratis', 'men'],
                        ['men', 'Hence'],
                        ['Hence', 'Socratis'],
                        ['Socratis', 'mortal']]
        self.assertListEqual(utils.generate_n_grams(line_split, 2), result_2gram)
    
    def test_generate_3_gram(self):
        result_3gram = [['men', 'mortal', 'Socratis'],
                        ['mortal', 'Socratis', 'men'],
                        ['Socratis', 'men', 'Hence'],
                        ['men', 'Hence', 'Socratis'],
                        ['Hence', 'Socratis', 'mortal']]
        self.assertListEqual(utils.generate_n_grams(line_split, 3), result_3gram)

