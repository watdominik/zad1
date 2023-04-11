import unittest
from main import EmailExtractorTestCase

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(EmailExtractorTestCase)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)