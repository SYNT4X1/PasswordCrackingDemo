import hashlib

PlainText = "Dictionary.txt"
HashedText = "Hashed.txt"

with open(PlainText,"r") as file:
    lines = file.readlines()
    hashed = open(HashedText, "a")
    for line in lines:
        hashedString = hashlib.sha256(line.strip('\n').encode('utf-8')).hexdigest()
        hashed.write(hashedString+'\n')
        