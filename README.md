# Unessay-CPSC-329-
#Author: Anh Tuan Pham && Alex Tran (https://github.com/tranalex)
Instructions

There are 2 problem questions: Caesar Decrypt (Easy) and Bifid Decrypt (Easy-Medium). 

The user will have to write their solution in caesarDecrypt.py and bifidDecrypt.py. The associated tests connected to these files (test_caesarDecrypt.py and test_bifidDecrypt.py) can then be run either in an IDE or the command line by “cding” into the given directory containing the tests and typing <python test_caesarDecrypt.py> or <python test_bifidDecrypt.py>. 

There are written and coded solutions in the solutions folders of each problem. The same set of tests for the solutions are also provided to show that they pass the given tests. They can be run in an IDE or by “cding” into the solution directory and typing <python test_caesarDecryptSolution.py> or <python test_bifidDecryptSolution.py>.

Tests Overview
test_caesarDecrypt contains 3 different tests.
1)	test_ciphertext 
It tests 4 different ciphertexts with the same key and shift.
Test Cases: full sentence, empty string, all special characters, all characters in key

2)	test_shift
It tests 3 different shifts with the same ciphertext and same key.
Test Cases: negative shift, 0 shift, positive shift

3)	test_key
It tests 3 different keys with the same ciphertext and same shift.
Test Cases: 3 different keys 

test_bifidDecrypt contains 2 different tests.
1)	test_ciphertext
It tests 5 different ciphertexts with the same polybius square.
Test Cases: full sentence, single character, empty string, special characters only, and all character in the polybius square

2)	test_polybiusSquare
It tests 3 different, randomized 6x6 polybius squares with the same ciphertext.
