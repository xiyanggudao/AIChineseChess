import os
import unittest


def load_tests(loader, standard_tests, pattern):
	testsDir = os.path.dirname(__file__)
	pattern = pattern or "Test*.py"
	projectDir = os.path.dirname(os.path.dirname(testsDir))
	package_tests = loader.discover(start_dir=testsDir, pattern=pattern, top_level_dir=projectDir)
	standard_tests.addTests(package_tests)
	return standard_tests


if __name__ == '__main__':
	unittest.main()
