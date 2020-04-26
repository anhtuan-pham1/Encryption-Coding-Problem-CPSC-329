def caesarDecrypt(key, ciphertext, shift):
        """Decrypt the string and return the plaintext"""
        
        plaintext = ''

        for char in ciphertext:
            try:
                i = (key.index(char) - shift) % len(key)
                plaintext += key[i]
            except ValueError:
                plaintext += char


        return plaintext


print(caesarDecrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "JK", 2))
