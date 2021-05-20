import unittest
import joseph_hanson_hw1

pif = joseph_hanson_hw1.print_if_leap
class testLeapYear(unittest.TestCase):
    def test_leap_years_true(self):
        self.assertEqual(pif(1804), True)
        self.assertEqual(pif(1908), True)
        self.assertEqual(pif(1884), True)
        self.assertEqual(pif(2012), True)
    def test_leap_years_false(self):
        self.assertEqual(pif(1803), False)
        self.assertEqual(pif(1909), False)
        self.assertEqual(pif(1885), False)
        self.assertEqual(pif(2013), False)

if __name__=='__main__':
    unittest.main()