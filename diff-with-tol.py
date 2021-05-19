# Author : Ali Snedden
# Date   : 5/14/21
# License: MIT
# Notes  : 
#
# Background : 
#       
# Purpose :
#   I have two files with numeric values. They aren't exact, but I want to see  
#   if they are close within a tolerance.
# 
#   
# How to Run :
import sys
import numpy as np
import time
import re
# my code
from error import exit_with_error



def print_help(Arg):
    """
    ARGS:
        Arg     : int, exit value
    DESCRIPTION:
        Print Help. Exit with value arg
    RETURN:
        N/A
    DEBUG:
        1. Tested, it worked
    FUTURE:
    """
    sys.stdout.write(
        "\nUSAGE : python diff-with-tol.py <file1> <file2> <sep> [tol1,tol2,...,tolN]\n\n"
        "   <file1>         : A file to compare, with N columns\n"
        "   <file2>         : A file to compare, with N columns\n"
        "   <sep>           : separator e.g. ',', ' '\n"
        "   [tol1,...,tolN] : optional, the fractional tolerance (rtol) for each N\n"
        "                     column. Uses np.isclose(rtol, atol=1e-10000).\n"
        "                     Default : rtol=0\n"
        "                         \n")
    sys.exit(Arg)


def main():
    """
    ARGS:
        None.
    DESCRIPTION:
    RETURN:
    DEBUG:
    FUTURE:
    """
    ######### Get Command Line Options ##########
    if(len(sys.argv) != 4 and len(sys.argv) != 5 and len(sys.argv) != 2) : 
        print_help(1)
    elif(len(sys.argv) == 2 and "-h" in sys.argv[1]):
        print_help(0)
    # Check python version
    if(sys.version_info[0] != 3):
        exit_with_error("ERROR!!! Wrong python version ({}), version 3 "
                        "expected\n".format(sys.version_info[0]))
    ### Timing info
    print("Started : %s"%(time.strftime("%D:%H:%M:%S")))
    startTime = time.time()
    isSame = True

    ### Get arguments
    f1path = sys.argv[1]    # path to file 1
    f2path = sys.argv[2]    # path to file 2
    sep    = sys.argv[3]    # separator, a string
    if(len(sys.argv) == 5):
        tolL = sys.argv[4].split(',')  # A list
        tolL = [float(tol) for tol in tolL]
    else:
        tolL = []
    
    
    ### Read files
    atol = 1e-10000
    data1L = []
    data2L = []
    f1 = open(f1path, "r")
    f2 = open(f2path, "r")
    # File 1
    for line in f1:
        # Remove new line characters
        line = line.strip()
        # Strip extra seperators
        lineL = [elem.strip(sep) for elem in line.split(sep)]
        # Remove empty elements
        lineL = [elem for elem in lineL if len(elem) > 0]
        N1    = len(lineL)
        for i in range(N1):
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
        lineL = [elem.strip(sep) for elem in line.split(sep)]
        # Remove empty elements
        lineL = [elem for elem in lineL if len(elem) > 0]
        N2    = len(lineL)
        for i in range(N2):
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
                # 
                except TypeError:
                    if(elem1 != elem2):
                        print("line {} : {} vs. {}".format(i, line1L, line2L))
                        isSame = False
    f1.close()
    f2.close()


    print("Ended   : %s"%(time.strftime("%D:%H:%M:%S")))
    print("Run Time : {:.4f} h".format((time.time() - startTime)/3600.0))
    if(isSame == True):
        print("\n\nFiles are IDENTICAL")
    else:
        print("\n\nFiles are DIFFERENT")
    sys.exit(0)


if __name__ == "__main__":
    main()

