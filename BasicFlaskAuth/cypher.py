# Import Package
from cryptography.fernet import Fernet
# Generate a Key and Instantiate a Fernet Instance
key = Fernet.generate_key()
f = Fernet(key)
print(key)
# Define our message
plaintext = b"encryption is very useful"
# Encrypt
ciphertext = f.encrypt(plaintext)
print(ciphertext)
# Decrypt
decryptedtext = f.decrypt(ciphertext)
print(decryptedtext)


key = b'8cozhW9kSi5poZ6TWFuMCV123zg-9NORTs3gJq_J5Do='
f = Fernet(key)
#print(key)
# Define our message
message = b'encrypting is just as useful'
# Encrypt
ciphertext = f.encrypt(message)
print(ciphertext)
# Decrypt
#ciphertext = b'gAAAAABc8Wf3rxaime-363wbhCaIe1FoZUdnFeIXX_Nh9qKSDkpBFPqK8L2HbkM8NCQAxY8yOWbjxzMC4b5uCaeEpqDYCRNIhnqTK8jfzFYfPdozf7NPvGzNBwuuvIxK5NZYJbxQwfK72BNrZCKpfp6frL8m8pdgYbLNFcy6jCJBXATR3gHBb0Y='
#decryptedtext = f.decrypt(ciphertext)
#print(decryptedtext)
