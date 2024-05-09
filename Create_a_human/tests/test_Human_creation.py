import unittest
from source.human_creation import Human

class HumanTest(unittest.TestCase):

    def testIntroduceYourself(self):
        self.human_01 = Human("Adam")
        # test the 'intorduce yourself' method
        # check if it returns expected text
        self.assertEqual("Hello, my name is Adam.", self.human_01.introduce_yourself())

        self.human_02 = Human("Eve")
        self.assertEqual("Hello, my name is Eve.", self.human_02.introduce_yourself())