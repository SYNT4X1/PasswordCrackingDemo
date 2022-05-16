Currently Hashgen is a way to generate sha256 hashes in bulk with a file using
newlines as a delimiter for each string. I used this as a function to generate
mass hashes when testing. The BF tag (xxxBF.txt) signifies the data for testing
with bruteforce. The bruteforce data set is designed with random data, so unless
random data is generated for the dictionary and collides with the hashed data
it's basically null and void for this. However, using the bruteforce script or
dictionary attack script will work for typical passwords. The top 100 passwords
from rockyou.txt have been hashed and tested for dictionary, following tag is
respective (xxxDC.txt). Have Fun!