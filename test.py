import unittest
import script
# import main


class TestMain(unittest.TestCase):
    #setUp is useful if you need to set up something before EACH function. 
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)

# can run more test
# see unittest documentation: https://docs.python.org/3/library/unittest.html
#     def test_do_stuff_2(self):
#         test_param = 'Mariea'
#         result = script.do_stuff(test_param)
#         self.assertTrue(isinstance(result, ValueError))
    def test_do_stuff_2(self):
        test_param = 'jhgjhf'
        result = script.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff_3(self):
        test_param = None
        result = script.do_stuff(test_param)
        self.assertEqual(result, "_please, enter a number_")

    def test_do_stuff_4(self):
        test_param = ''
        result = script.do_stuff(test_param)
        self.assertEqual(result, "_please, enter a number_")


if __name__ == '__main__':
    unittest.main()
