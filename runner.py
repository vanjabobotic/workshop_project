from unittest import defaultTestLoader
from utilities import config
from utilities import runners
import sys

# SELECT TEST RUNNER
if config.report:
    test_runner = runners.html_test_runner

else:
    test_runner = runners.text_test_runner

# SELECT TEST SUITE
if config.scope is not None:
    test_suite = defaultTestLoader.loadTestsFromName(config.scope)
else:
    test_suite = defaultTestLoader.discover("./tests/", "*_tests.py")

# RUN TESTS
test_results = test_runner.run(test_suite)

if not test_results.wasSuccessful():
    sys.exit(-1)
