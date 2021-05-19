# diff-with-tol

### Purpose : 
This code is a python script that can identify differences between two files.
It is particularly useful because :
1. You can use relative thresholds for each column to determine whether the files
   are identical or not. This sidesteps the issue of comparing files with very close
   but NOT identical floating point values
2. This file can compare files with both floating point and string data types.

### Installation :
1. Be sure you have `python3` and `numpy` installed
2. Clone this repo and then run `diff-with-tol.py`

### Usage : 
For a file with `N` columns, the format is :

`python diff-with-tol.py <file1> <file2> <sep> [tol1,tol2,...,tolN]`

Where : 
1. `file1` and `file1` are input files
2. `<sep>` is the field seperator, typically things like ',' or ' ' or ';'
3. `[tol1,tol2,...,tolN]` is the relative tolerance for each column

E.g. `python diff-with-tol.py data/dat1.txt data/dat2.txt ' ' 0.09,0.05,0.002`
