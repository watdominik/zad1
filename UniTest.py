import unittest
from main import EmailExtractorTestCase

class UniTest(unittest.TestSuite):
    def __init__(self):
        super().__init__()
        self.addTests(unittest.makeSuite(EmailExtractorTestCase))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    uni_test = UniTest()
    runner.run(uni_test)