"""
Created on Oct 2, 2018

@author: craciunv
"""
import unittest
from blackjack import card


class TestCard(unittest.TestCase):
    """Class doc-string"""

    def test_card_print(self):
        """Method doc-string"""

        test_card = card.Card('Two', 'Hearts')
        result = test_card.__str__()
        self.assertEqual(result, 'Two of Hearts')


if __name__ == '__main__':
    unittest.main()
