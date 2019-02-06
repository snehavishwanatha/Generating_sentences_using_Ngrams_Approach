The project concentrates on a simple approach of generating sentences based on any given datasets which are paragraphs of related content using the concept of N-grams.


<----------TO RUN THE PROGRAM------------>

FROM UBUNTU TERMINAL RUN the file "generate.py" using following command ->
$ python3 generate.py


Note: Text Data is present within the python file generate.py itself, so no need of seperate .txt file.


PRE-REQUSITES:
Installing NLTK
NLTK requires Python versions 2.7, 3.4, 3.5, 3.6, or 3.7

*Mac/Unix¶
Install NLTK: run sudo pip install -U nltk
Install Numpy (optional): run sudo pip install -U numpy
Test installation: run python then type import nltk
For older versions of Python it might be necessary to install setuptools (see http://pypi.python.org/pypi/setuptools) and to install pip (sudo easy_install pip).

*Windows
These instructions assume that you do not already have Python installed on your machine.

32-bit binary installation
Install Python 3.7: http://www.python.org/downloads/ (avoid the 64-bit versions)
Install Numpy (optional): https://www.scipy.org/scipylib/download.html
Install NLTK: http://pypi.python.org/pypi/nltk
Test installation: Start>Python37, then type import nltk
Installing Third-Party Software
Please see: https://github.com/nltk/nltk/wiki/Installing-Third-Party-Software

Also required NLTK packages need to be installed for tokenisation and n-grams.

