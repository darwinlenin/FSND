# Import the Python Library
import bcrypt
import sys

password = b"studyhard"
# Hash a password for the first time, with a certain number of rounds
salt = bcrypt.gensalt(14)
hashed = bcrypt.hashpw(password, salt)
print(salt)
print(hashed)
# Check a plain text string against the salted, hashed digest
bcrypt.checkpw(password, hashed)

passwordTwo = b"learningisfun"
hashed = b'$2b$14$EFOxm3q8UWH8ZzK1h.WTZeRcPyr8/X0vRfuL3/e9z7AKIMnocurBG'
# Check a plain text string against the salted, hashed digest
print(bcrypt.checkpw(passwordTwo, hashed))
