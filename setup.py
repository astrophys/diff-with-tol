# Author : Ali Snedden
# Date   : 6/19/22
# License: MIT
from distutils.core import setup

setup(name='diffwtol',
      version='0.1.0',
      description='Difference between files within tolerance',
      author='Ali Snedden',
      author_email='ali.snedden [at] nationwidechildrens.org',
      url='https://github.com/astrophys/diff-with-tol',
      packages=['diffwtol'],
      install_requires=[
        "numpy"
      ],
     )
