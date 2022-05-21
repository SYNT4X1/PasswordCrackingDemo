import random
import hashlib
import string

SupportedChars = string.ascii_letters + string.digits # Add to this to keep testing characters for permutations

def BadUserAttack(username,DatabaseFile = "Demo/Database.txt"):
    successful = []
    with open(DatabaseFile) as HashedText: # File reading, will close when all is done
        Hashed = HashedText.readlines()
        for HashedLine in Hashed:
            if username in HashedLine:
                BareHash = HashedLine.strip('\n') # the newline can make things tricky, so I just took it out
                # print("[ Hashed ] ", BareHash) # if you want the hash being tested as output, just clutters screen in my opinion
                Hashing = True
                while (Hashing):
                    randomLength = random.randint(1, 16)
                    randomString = ''.join(random.choices(SupportedChars, k = randomLength))
                    HashedString = hashlib.sha256(''.join(randomString).strip('\n').encode('utf-8')).hexdigest() # calculate hash of permutation
                    if HashedString in BareHash: # test hash
                        print("[ Success ] ", ''.join(randomString)," | " , HashedString)
                        successful.append(randomString)
                        Hashing = False
                        break
                    else:
                        print("[ Failed ] ", ''.join(randomString)," | " , HashedString) # print out the failures, just screen clutter
                        continue

        for hit in successful:
            print("[ Success ] ", hit.strip('\n')," | ", username)
