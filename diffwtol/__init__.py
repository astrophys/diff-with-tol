"""Module that compares two files for identity within a tolerance (if specified).

This module is particulary useful in providing Linux diff-like behavior but
with the advantage being able to compare two files for identity within a
particular tolerance. Can handle mixed data with both strings and floats

Can be run by importing as a module or from the command line directly with
diff_with_tol.py
"""

__version__ = "0.1.0"

from .diff_with_tol import diff_two_files_with_tol
from .error import exit_with_error
#from .unittest_diff_with_tol import TEST_DIFF_W_TOL
__all__ = [
        'diff_two_files_with_tol',
        'exit_with_error',
#        'TEST_DIFF_W_TOL'
        ]


