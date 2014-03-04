from awesome_sum import awesome_sum
import unittest

class AwesomeSumTest(unittest.TestCase):
    def test_one_plus_one(self):
        self.assertEqual(2, awesome_sum(1,1))

    # You can add more tests cases here

if __name__ == '__main__':
    unittest.main()