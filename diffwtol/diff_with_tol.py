# Author : Ali Snedden
# Date   : 5/14/21
# License: MIT
"""Module that compares two files for identity within a tolerance (if specified).

This module is particulary useful in providing Linux diff-like behavior but
with the advantage being able to compare two files for identity within a
particular tolerance. Can handle mixed data with both strings and floats
"""
import sys
import time
import argparse
import numpy as np
#from error import exit_with_error
from diffwtol.error import exit_with_error


def diff_two_files_with_tol(Path1=None, Path2=None, Sep=None, TolL=None):
    """
    Compares two files for identity within the tolerance (if specified)

    Args:
        Path1 : (str) path to file 1
        Path2 : (str) path to file 2
        Sep   : (str) separator
        TolL  : (list of floats) optional, tolerances for each column. E.g. if
                specified, for a 3 column file would have 3 floats in the list

    Returns:
        isSame: (bool) if the files are the same or not.
                If false, prints differences to stdout as well
    """
    ### Read files
    atol = 1e-10000
    data1L = []
    data2L = []
    f1 = open(Path1, "r")
    f2 = open(Path2, "r")
    isSame = True
    if(TolL is None):
        tolL = []
    else:
        tolL = TolL
    #print("tolL = {}".format(tolL))
    # File 1
    for line in f1:
        # Remove new line characters
        line = line.strip()
        # Strip extra seperators
        lineL = [elem.strip(Sep) for elem in line.split(Sep)]
        # Remove empty elements
        lineL = [elem for elem in lineL if len(elem) > 0]
        n1    = len(lineL)
        for i in range(n1):
            try :
                lineL[i] = float(lineL[i])
            except ValueError :
                lineL[i] = str(lineL[i])
        data1L.append(lineL)
    # File 2
    for line in f2:
        # Remove new line characters
        line = line.strip()
        # Strip extra seperators
        lineL = [elem.strip(Sep) for elem in line.split(Sep)]
        # Remove empty elements
        lineL = [elem for elem in lineL if len(elem) > 0]
        n2    = len(lineL)
        for i in range(n2):
            try :
                lineL[i] = float(lineL[i])
            except ValueError :
                lineL[i] = str(lineL[i])
        data2L.append(lineL)

    ### Compare
    # Are they the same length?
    if(len(data1L) != len(data2L)):
        exit_with_error("ERROR!!! len(data1L) {} != len(data2L) {}\n".format(
                        len(data1L), len(data2L)))
    # Loop through and compare
    for i in range(len(data1L)):
        line1L = data1L[i]
        line2L = data2L[i]
        # Element should be the same size
        if(len(line1L) != len(line2L)):
            print("line {} : {} vs. {}\n".format(i,line1L, line2L))
            isSame = False
        for j in range(len(line1L)):
            elem1 = line1L[j]
            elem2 = line2L[j]
            ### Is Tolerance Set?
            if(len(tolL) == 0):
                # Are the elements EXACTLY the same?
                if(elem1 != elem2):
                    print("line {} : {} != {}".format(i, line1L, line2L))
                    isSame = False
            ### Are the elements within tolerance?
            else:
                rtol = tolL[j]
                # Float
                try:
                    if(np.isclose(elem1, elem2, rtol=rtol, atol=atol) == False):
                        print("line {} : {} vs. {}".format(i, line1L, line2L))
                        isSame = False
                except TypeError:
                    if(elem1 != elem2):
                        print("line {} : {} vs. {}".format(i, line1L, line2L))
                        isSame = False
    f1.close()
    f2.close()
    #print("isSame={}".format(isSame))
    return(isSame)


def main():
    """
    Prints to stdout whether two files are identical within the tolerance

    Args:
        None.

    Returns:
        None
    """
    ### Get Command Line Options
    parser = argparse.ArgumentParser(description='Compare files that are numerically'
                                                 'close but not identical')
    parser.add_argument('f1path', metavar='file1', type=str, help='first file')
    parser.add_argument('f2path', metavar='file2', type=str, help='second file')
    parser.add_argument('sep',    metavar='sep',   type=str, help='Separator, e.g. ","')
    parser.add_argument('tolL',   metavar='tol',   type=float, nargs="*",
                        help='Tolerance, if absent look for exact comparison, otherwise'
                              'pass float for each column')
    args = parser.parse_args()

    ### Timing info
    print("Started : {}".format(time.strftime("%D:%H:%M:%S")))
    startTime = time.time()

    ### Get arguments
    f1path = args.f1path                    # path to file 1
    f2path = args.f2path                    # path to file 2
    sep    = args.sep                       # separator, a string
    if(args.tolL is not None):
        tolL   = args.tolL                  # List of tolerances
    else:
        tolL   = []

    isSame = diff_two_files_with_tol(Path1=f1path, Path2=f2path, Sep=sep, TolL=tolL)

    # Print timing information
    print("Ended   : %s"%(time.strftime("%D:%H:%M:%S")))
    print("Run Time : {:.4f} h".format((time.time() - startTime)/3600.0))
    if(isSame is True):
        print("\n\nFiles are IDENTICAL")
    else:
        print("\n\nFiles are DIFFERENT")
    sys.exit(0)


if __name__ == "__main__":
    main()
