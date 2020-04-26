import unittest
import bifidDecryptSolution

class TestBifid(unittest.TestCase):
    
    def test_cipherText(self):
        #Tests different ciphertexts with the same 6x6 polybius square
        sixBysix =[['B','G','0','W','K','Z'],
                  ['Q','1','P','L','D','S'],
                  ['9','I','O','X','7','E'],
                  ['F','4','C','U','M','6'],
                  ['T','H','2','V','R','5'],
                  ['N','A','8','Y','3','J']
                 ]

        #Ciphertexts
        fullSentence = "21XJY, OS P952 SX 5YIY! CVG5 SL Y4QS CMG5?"
        singleCharacter = "A"
        emptyString = ""
        specialCharactersOnly = "?!><.@#$%^&*()"
        allCharactersInSquare = "ZHPF8LI4US1NC6KDYA79JME2GTO3VRQB0W5X"
        
        #Tests
        self.assertEqual(bifidDecryptSolution.bifidDecrypt(sixBysix,fullSentence),"HELLO, MY NAME IS ALEX! WHAT IS YOUR NAME?")
        self.assertEqual(bifidDecryptSolution.bifidDecrypt(sixBysix,singleCharacter),"A")
        self.assertEqual(bifidDecryptSolution.bifidDecrypt(sixBysix,emptyString),"")
        self.assertEqual(bifidDecryptSolution.bifidDecrypt(sixBysix,specialCharactersOnly),"?!><.@#$%^&*()")
        self.assertEqual(bifidDecryptSolution.bifidDecrypt(sixBysix,allCharactersInSquare),"032QSEUK8EDC91MQCCS3DL3K49FNB2QV368L")

    def test_polybiusSquare(self):    
        #Tests 3 different, randomized 6x6 polybius squares with the same ciphertext
        polybiusSquareA = [['0','J','7','N','V','Q'],
             ['F','L','Z','A','O','W'],
             ['S','1','P','H','9','C'],
             ['X','6','Y','3','M','E'],
             ['R','D','8','U','I','B'],
             ['4','K','5','T','G','2']
            ]

        polybiusSquareB = [['4','8','P','U','W','K'],
            ['6','J','R','E','S','9'],
            ['N','X','O','C','D','L'],
            ['Q','M','3','1','I','V'],
            ['5','0','F','Y','T','B'],
            ['7','Z','2','G','A','H']
            ]   
        
        polybiusSquareC = [['S','K','V','P','T','0'],
            ['I','O','7','1','U','3'],
            ['W','6','D','4','J','F'],
            ['C','Y','G','M','X','H'],
            ['2','R','B','9','A','5'],
            ['Z','Q','L','N','8','E']
            ]

        #Ciphertexts
        cipherTextA = "HLAXA, M1 A61G HO RA3K! O83B R6 4T3R 9X3B?"
        cipherTextB = "ZOCFG, E9 XNHY SN RG9V! 2EWE TB MBTT 33WE?"
        cipherTextC = "HE1H9, QT EGXK PO 59EL! 6YXH SB 80AS ORXH?"

        #Tests
        self.assertEqual(bifidDecryptSolution.bifidDecrypt(polybiusSquareA,cipherTextA),"HELLO, MY NAME IS ALEX! WHAT IS YOUR NAME?")
        self.assertEqual(bifidDecryptSolution.bifidDecrypt(polybiusSquareB,cipherTextB),"HELLO, MY NAME IS ALEX! WHAT IS YOUR NAME?")
        self.assertEqual(bifidDecryptSolution.bifidDecrypt(polybiusSquareC,cipherTextC),"HELLO, MY NAME IS ALEX! WHAT IS YOUR NAME?")

#Allows test to be called directly from command line
if __name__ == '__main__':
    unittest.main()

    
