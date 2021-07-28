import unittest
import sys
sys.path.append('./src')
from src.renamer import Renamer

class TestRenamer(unittest.TestCase):
    def test_renamer(self):
        """ Test Renamer class """
        renamer = Renamer('./src/anim', name="anim", seq=5)

if __name__ == '__main__':
    unittest.main()
