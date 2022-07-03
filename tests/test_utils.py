from packages import utils
import unittest

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
        word = "All men are mortal. Socrates is a men. Hence, Socrates is mortal"
        should_match = 'all men are mortal socrates is a men hence socrates is mortal'
        self.assertEqual(utils.remove_punctuation(word), should_match)
    
    def test_n_gram_freq(self):
        test_input = [['men'],
                        ['mortal'],
                        ['Socrates'],
                        ['men'],
                        ['Hence'],
                        ['Socrates'],
                        ['mortal']]
        result = [('mortal', 2), ('men', 2), ('Socrates', 2), ('Hence', 1)]
        self.assertListEqual(utils.n_gram_freq(test_input), result)
    
    def test_remove_state_name(self):
        query_list = ['he is in new york', 'she is in town', 'oh no florida']
        should_be = ['she is in town']
        self.assertListEqual(utils.remove_state_name(query_list), should_be)
    
    def test_has_state_name(self):
        query1 =  'going to new york'
        query2 = 'not going to Maryland'
        query3 = 'not going at all'
        self.assertEqual(utils.has_state_name(query1), True)
        self.assertEqual(utils.has_state_name(query2), True)
        self.assertEqual(utils.has_state_name(query3), False)


  
class TestGenerateNgram(unittest.TestCase):
    def test_generate_ngram(self):
        clean_line = ['men mortal socrates men hence socrates mortal']
        result_1gram =     [['men'], ['mortal'], ['socrates'], ['men'], ['hence'], ['socrates'],['mortal']]
        result_2gram = [['men', 'mortal'], ['mortal', 'socrates'], ['socrates', 'men'], ['men', 'hence'],                   ['hence', 'socrates'], ['socrates', 'mortal']]
        result_3gram = [['men', 'mortal', 'socrates'],
                            ['mortal', 'socrates', 'men'], ['socrates', 'men', 'hence'],
                            ['men', 'hence', 'socrates'], ['hence', 'socrates', 'mortal']]
        self.assertListEqual(utils.generate_n_grams(clean_line, 1), result_1gram)
        self.assertListEqual(utils.generate_n_grams(clean_line, 2), result_2gram)
        self.assertListEqual(utils.generate_n_grams(clean_line, 3), result_3gram)

