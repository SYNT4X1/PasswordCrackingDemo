import time
import string 
import hashlib
from itertools import permutations

from websockets import Data

SupportedChars = string.ascii_letters + string.digits # Add to this to keep testing characters for permutations

def DictionaryAttack(HashFile = "Dictionary/HashedDC.txt", DictionaryFile = "Dictionary/Dictionary.txt"):
    with open(HashFile) as HashedText, open(DictionaryFile) as DictionaryText: # File reading, will close when all is done
        Hashed = HashedText.readlines()
        Dictionary = DictionaryText.readlines()
        for HashedLine in Hashed:
            BareHash = HashedLine.strip('\n')
            for Dict in Dictionary:
                HashedString = hashlib.sha256(''.join(Dict).strip('\n').encode('utf-8')).hexdigest()
                if HashedString == BareHash: # test hash
                    print("[ Success ] ", ''.join(Dict).strip('\n')," | " , HashedString)
                    break
                else:
                    continue

def DictionaryAttackUser(username, DictionaryFile = "Dictionary/Dictionary.txt", Database = "Demo/Database.txt",):
    successful = []
    with open(Database) as Database, open(DictionaryFile) as DictionaryText: # File reading, will close when all is done
        Hashed = Database.readlines()
        Dictionary = DictionaryText.readlines()
        for HashedLine in Hashed:
            if username in HashedLine:
                BareHash = HashedLine.strip('\n')
                for Dict in Dictionary:
                    HashedString = hashlib.sha256(''.join(Dict).strip('\n').encode('utf-8')).hexdigest()
                    if HashedString in BareHash: # test hash
                        print("[ Success ] ", ''.join(Dict).strip('\n')," | " , HashedString)
                        successful.append(Dict)
                        break
                    else:
                        print("[ Failed ] ", ''.join(Dict).strip('\n')," | " , HashedString)
                        continue

    print("=====\n[#] SUMMARY\n=====")
    for hit in successful:
        print("[ Success ] ", hit.strip('\n')," | ", username)

# DictionaryAttackUser("test") #demo for class