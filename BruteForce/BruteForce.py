import time
import string 
import hashlib
from itertools import permutations

SupportedChars = string.ascii_letters + string.digits # Add to this to keep testing characters for permutations
HashFile = "BruteForce/HashedBF.txt" # input file of Hashed Passwords in sha256


print("==========\n[ STATUS ]: Started...\n==========")
start = time.time() # begin timer

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

print("==========\n[ STATUS ]: Done...\n==========")
end = time.time()
print("Completed in: ",end - start)
