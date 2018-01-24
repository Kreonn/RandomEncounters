import sys
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    """Setup the pytest test runner."""

    def finalize_options(self):
        """Set options for the command line."""
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """Execute the test runner command."""
        import pytest
        sys.exit(pytest.main(self.test_args))
