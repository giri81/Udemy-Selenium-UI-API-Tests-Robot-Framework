# run_all_tests.py

import unittest

# Discover and run all the tests
if __name__ == "__main__":
    # Create a test loader
    loader = unittest.TestLoader()

    # Discover tests in the current directory
    tests = loader.discover(start_dir='.', pattern='test_*.py')

    # Create a test runner that will display the results
    runner = unittest.TextTestRunner(verbosity=2)

    # Run the tests
    runner.run(tests)
