from ordstjerneSolver import ordstjerne_solver
import unittest
import pandas as pd

# Constants
FULLFORMSLISTE_PATH = "fullformsliste.csv"
COLUMN_TAG_OPPSLAG = "OPPSLAG"
ALLOWED_LETTERS = ["i", "o", "u", "ø", "t", "n", "k"]
MUST_HAVE = "k"

# Dictionary
fullformsliste = pd.read_csv(FULLFORMSLISTE_PATH)


class TestOrdStjerneSolver(unittest.TestCase):
    def test_ordstjerne_solver(self):
        result = ordstjerne_solver(ALLOWED_LETTERS, MUST_HAVE)
        self.assertEqual(len(result), 50)


if __name__ == "__main__":
    unittest.main()
