import time
import string 
import hashlib
from itertools import permutations

SupportedChars = string.ascii_letters + string.digits # Add to this to keep testing characters for permutations
HashFile = "Dictionary/HashedDC.txt" # input file of Hashed Passwords in sha256
DictionaryFile = "Dictionary/Dictionary.txt"

print("==========\n[ STATUS ]: Started...\n==========")
start = time.time() # begin timer

with open(HashFile) as HashedText, open(DictionaryFile) as DictionaryText: # File reading, will close when all is done
    Hashed = HashedText.readlines()
    Dictionary = DictionaryText.readlines()
    for HashedLine in Hashed:
        BareHash = HashedLine.strip('\n')
        for Dict in Dictionary:
            HashedString = hashlib.sha256(''.join(Dict).strip('\n').encode('utf-8')).hexdigest()
            if HashedString == BareHash: # test hash
                print("[ Success ] ", ''.join(Dict).strip('\n')," | " , HashedString)
                Hashing = False
                break
            else:
                continue

print("==========\n[ STATUS ]: Done...\n==========")
end = time.time()
print("Completed in: ",end - start)
