import random

# A function to shuffle all of the characters
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# Generate a random uppercase letter
uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65,90))
uppercaseLetter3 = chr(random.randint(65,90))


# Generate a random lowercase letter
lowercaseLetter1 = chr(random.randint(97, 122))
lowercaseLetter2 = chr(random.randint(91, 122))
lowercaseLetter3 = chr(random.randint(91, 122))
lowercaseLetter4 = chr(random.randint(91, 122))

# Generate a random number
digit1 = chr(random.randint(48, 57))
digit2 = chr(random.randint(48, 57))
digit3 = chr(random.randint(48, 57))

# Generate a random punctuation sign
punctuationSign1 = chr(random.randint(33, 152))
punctuationSign2 = chr(random.randint(33, 152))

password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationSign1 +punctuationSign2 + uppercaseLetter3 + lowercaseLetter3 + lowercaseLetter4 + digit3
password = shuffle(password)

print(password)