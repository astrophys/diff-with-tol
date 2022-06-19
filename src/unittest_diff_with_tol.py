# Author : Ali Snedden
# Date   : 6/19/22
# License: MIT
"""Module that unit tests the module diff-with-tol.py:diff_two_files_with_tol()

This module tests the function diff_two_files_with_tol() with several unit 
cases to ensure the thresholding and string comparison works.
"""
import sys
import time
import argparse
import unittest
#import numpy as np
from error import exit_with_error
from diff_with_tol import diff_two_files_with_tol



class TEST_DIFF_W_TOL(unittest.TestCase):
    """
    Tests variety of cases to ensure thresholding and string comparison works

    Args:
        unittest.TestCase

    Returns:
        N/A
    """
    def test_diff_two_files_with_tol(self):
        """
        Checks for equality in several cases

        Args:
            self : 

        Returns:
            N/A
        """
        ##### Test Identical case #####
        result = diff_two_files_with_tol(Path1="data/same-f1.txt",
                                         Path2="data/same-f2.txt", Sep=' ',
                                         TolL=[])
        self.assertEqual(result, True)
        ##################################
        ##### FLOAT TESTING WITH TOL #####
        ##################################
        #
        ##### float diff in col 1 #####
        # w/in tol
        result = diff_two_files_with_tol(Path1="data/diff-col1-f1.txt",
                                         Path2="data/diff-col1-f2.txt", Sep=' ',
                                         TolL=[0.04,0,0])
        self.assertEqual(result, True)
        # outside tol
        result = diff_two_files_with_tol(Path1="data/diff-col1-f1.txt",
                                         Path2="data/diff-col1-f2.txt", Sep=' ',
                                         TolL=[0,0,0])
        self.assertEqual(result, False)
        ##### float diff in col 2 #####
        # w/in tol
        result = diff_two_files_with_tol(Path1="data/diff-col2-f1.txt",
                                         Path2="data/diff-col2-f2.txt", Sep=' ',
                                         TolL=[0,0.06,0])
        self.assertEqual(result, True)
        # outside tol
        result = diff_two_files_with_tol(Path1="data/diff-col2-f1.txt",
                                         Path2="data/diff-col2-f2.txt", Sep=' ',
                                         TolL=[0,0,0])
        self.assertEqual(result, False)
        ##### float diff in col 3 #####
        # w/in tol
        result = diff_two_files_with_tol(Path1="data/diff-col3-f1.txt",
                                         Path2="data/diff-col3-f2.txt", Sep=' ',
                                         TolL=[0,0,0.15])
        self.assertEqual(result, True)
        # outside tol
        result = diff_two_files_with_tol(Path1="data/diff-col3-f1.txt",
                                         Path2="data/diff-col3-f2.txt", Sep=' ',
                                         TolL=[0,0,0])
        self.assertEqual(result, False)

        
        ##################################
        ######### STRING TESTING #########
        ##################################
        #
        ##### str diff in col 1 #####
        # w/in tol
        result = diff_two_files_with_tol(Path1="data/diff-col1-str-f1.txt",
                                         Path2="data/diff-col1-str-f2.txt", Sep=' ')
        self.assertEqual(result, False)
        ##### str diff in col 2 #####
        # w/in tol
        result = diff_two_files_with_tol(Path1="data/diff-col2-str-f1.txt",
                                         Path2="data/diff-col2-str-f2.txt", Sep=' ')
        self.assertEqual(result, False)
        ##### str diff in col 3 #####
        # w/in tol
        result = diff_two_files_with_tol(Path1="data/diff-col3-str-f1.txt",
                                         Path2="data/diff-col3-str-f2.txt", Sep=' ')
        self.assertEqual(result, False)
                                                
        
        
        
        


if __name__ == "__main__":
    ### Timing info
    #print("Started : {}".format(time.strftime("%D:%H:%M:%S")))
    #startTime = time.time()
    unittest.main()
    # Print timing information
    #print("Ended   : %s"%(time.strftime("%D:%H:%M:%S")))
    #print("Run Time : {:.4f} h".format((time.time() - startTime)/3600.0))
    print("poo")
    sys.exit(0)
