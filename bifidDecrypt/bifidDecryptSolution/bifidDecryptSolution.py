def bifidDecrypt(polybiusSquare, cipherText):
    characterDict = {} #Characters in polybiusSquare
    positionDict = {} #Tuples containing row and column of each character in polybiusSquare
    plainText = "" #Resulting plaintext
    coordinateArray = [] #Holds the row and column of each character in the ciphertext in order

    #Fills characterDict and positionDict using the polybius square
    for row in range(0,len(polybiusSquare)):
        for col in range(0,len(polybiusSquare[0])):
            character = polybiusSquare[row][col]
            characterDict[character] = (row,col)
            positionDict[(row,col)] = character
  
    #Fills the coordinateArray with the row and column of each character in the ciphertext
    for char in cipherText:
        if (char.upper() in characterDict):
            charCoordinates = characterDict[char.upper()]
            coordinateArray.append(charCoordinates[0])
            coordinateArray.append(charCoordinates[1])

    #Decrypts the ciphertext
    cipherTextIndex = 0
    for char in cipherText:
        if (char.upper() in characterDict):
            coordinateLeft = coordinateArray[cipherTextIndex]
            coordinateRight = coordinateArray[cipherTextIndex+len(coordinateArray)//2]
            decryptedChar = positionDict[(coordinateLeft,coordinateRight)]
            plainText += decryptedChar
            cipherTextIndex += 1
        else: #If character is not in the characterDict, then it must be a special character
            plainText += char

    return plainText