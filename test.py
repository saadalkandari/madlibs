import io
import sys
from unittest.mock import patch
import unittest
import madlibs


class ContainersTestCase(unittest.TestCase):
    
    expected_stacks = "It was 5 o'clock when I heard a knock on the door. I opened the door and and there was a box full of book, with a note saying 'From Morty'. Just as I closed the door, someone screamed, 'APPLE CRUMBLE HAS APPLES'. I froze in place and all I could do was jump."
    
    @classmethod
    def setUpClass(cls):
        cls.user_input = ['12', 'stars', 'star lord', 'all the apples', 'jump']
        cls.capturedOutput = io.StringIO()
        sys.stdout = cls.capturedOutput
        with patch('builtins.input', side_effect=cls.user_input):
            stacks = madlibs.main()

    def test_time(self):
        self.assertTrue(self.user_input[0] in self.capturedOutput.getvalue())

    def test_items(self):
        self.assertTrue(self.user_input[1] in self.capturedOutput.getvalue())

    def test_name(self):
        self.assertTrue(self.user_input[2].title() in self.capturedOutput.getvalue())

    def test_scream(self):
        self.assertTrue(self.user_input[3].upper() in self.capturedOutput.getvalue())

    def test_action(self):
        self.assertTrue(self.user_input[4] in self.capturedOutput.getvalue())


if __name__ == '__main__':
    unittest.main()




