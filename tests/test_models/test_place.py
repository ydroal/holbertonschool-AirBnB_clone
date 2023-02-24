import unittest
from models.place import Place


class Test_Place(unittest.TestCase):
    '''Test class for Place class'''

    def test_place(self):
        pl = Place()
        self.assertEqual('', pl.name)
        self.assertEqual(0, pl.number_rooms)


if __name__ == "__main__":
    unittest.main()
