from ordstjerneSolver import isInWord, ordstjerne_solver
import unittest
import pandas as pd

# Constants
WORDS_PATH = "data/words.csv"
COLUMN_TAG_OPPSLAG = "OPPSLAG"
ALLOWED_LETTERS = ["i", "o", "u", "Ø", "t", "n", "k"]
MUST_HAVE = "k"

# Dictionary
fullformsliste = pd.read_csv(WORDS_PATH)


class TestOrdStjerneSolver(unittest.TestCase):
    def test_ordstjerne_solver(self):
        result = ordstjerne_solver(ALLOWED_LETTERS, MUST_HAVE)
        self.assertEqual(len(result), 50)

    def test_isInWord(self):
        result = isInWord(ALLOWED_LETTERS, "nøtt")
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
