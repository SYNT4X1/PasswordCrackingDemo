import time
import string 
import hashlib
from itertools import permutations

SupportedChars = string.ascii_letters + string.digits # Add to this to keep testing characters for permutations

def BruteForceFileAttack(HashFile = "BruteForce/HashedBF.txt"):
    with open(HashFile) as HashedText: # File reading, will close when all is done
        Hashed = HashedText.readlines()
        for HashedLine in Hashed:
            PasswordLength = 1;
            BareHash = HashedLine.strip('\n') # the newline can make things tricky, so I just took it out
            # print("[ Hashed ] ", BareHash) # if you want the hash being tested as output, just clutters screen in my opinion
            Hashing = True
            while (Hashing):
                Permutations = permutations(SupportedChars, PasswordLength) # calculate all permutations of accepted chars given the length
                for Perm in Permutations:
                    HashedString = hashlib.sha256(''.join(Perm).strip('\n').encode('utf-8')).hexdigest() # calculate hash of permutation
                    if HashedString == BareHash: # test hash
                        print("[ Success ] ", ''.join(Perm)," | " , HashedString)
                        Hashing = False
                        break
                    else:
                        # print("[ Failed ] ", ''.join(Perm)," | " , HashedString) # print out the failures, just screen clutter
                        continue
                    
                PasswordLength += 1 # if all else fails increment permuation length by one and retry

def BruteForceUserAttack(username,DatabaseFile = "Demo/Database.txt"):
    successful = []
    with open(DatabaseFile) as HashedText: # File reading, will close when all is done
        Hashed = HashedText.readlines()
        for HashedLine in Hashed:
            if username in HashedLine:
                PasswordLength = 1;
                BareHash = HashedLine.strip('\n') # the newline can make things tricky, so I just took it out
                # print("[ Hashed ] ", BareHash) # if you want the hash being tested as output, just clutters screen in my opinion
                Hashing = True
                while (Hashing):
                    Permutations = permutations(SupportedChars, PasswordLength) # calculate all permutations of accepted chars given the length
                    for Perm in Permutations:
                        HashedString = hashlib.sha256(''.join(Perm).strip('\n').encode('utf-8')).hexdigest() # calculate hash of permutation
                        if HashedString in BareHash: # test hash
                            print("[ Success ] ", ''.join(Perm)," | " , HashedString)
                            successful.append(Perm)
                            Hashing = False
                            break
                        else:
                            print("[ Failed ] ", ''.join(Perm)," | " , HashedString) # print out the failures, just screen clutter
                            continue
                        
                    PasswordLength += 1 # if all else fails increment permuation length by one and retry
        for hit in successful:
            print("[ Success ] ", hit.strip('\n')," | ", username)

# BruteForceFileAttack() # for demo in class