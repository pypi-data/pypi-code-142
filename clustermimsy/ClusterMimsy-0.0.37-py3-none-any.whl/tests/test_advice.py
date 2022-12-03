import unittest

import ClusterMimsy as cm

class TestAdvice(unittest.TestCase):
    def test_returns_string(self):
        s = cm.nest.advice.words_to_live_by('Lemons')
        self.assertTrue(isinstance(s, str))
    
    def test_returns_lemonade(self):
        s = cm.nest.advice.words_to_live_by('Lemons')
        self.assertEqual(s, 'Lemonade, obviously')
    
    def test_returns_chill(self):
        s = cm.nest.advice.words_to_live_by('Happiness')
        self.assertEqual(s, 'Just chill')
    
    def test_returns_ramenade(self):
        s = cm.nest.advice.words_to_live_by('Ramen')
        self.assertEqual(s, 'Ramenade')

if __name__ == '__main__':
    unittest.main()