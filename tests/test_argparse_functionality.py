"""Tests for all argparse functionality.

   isort:skip_file
"""
import sys

import hyperparse

# Override argparse module here, to make tests test hyperparse instead of
# argparse.
sys.modules["argparse"] = hyperparse

from test.test_argparse import *
