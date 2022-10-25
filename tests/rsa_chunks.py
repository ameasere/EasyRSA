"""
Testing RSA encryption and decryption with chunks.
"""

import rsa
import time
import os

# Test 1
# 1. Generate a key pair
# 2. Start timer
# 3. Encrypt a message
# 4. Stop timer
# 5. Print time

print(u"\u001b[35;1m Test 1: Key size on the same file. \u001b[0m")

(publicKey, privateKey) = rsa.newkeys(512)
with open('rsa_chunks\\wordlist1.txt', 'rb') as f:
    message = f.read()
    # Start timer
    start = time.perf_counter()
    # Read file in 512 bit chunks
    for chunk in iter(lambda: f.read(512), b''):
        # Encrypt chunk
        crypto = rsa.encrypt(chunk, publicKey)
        print(crypto)
    # End timer
    end = time.perf_counter()
    f.close()
    print(u"\u001b[32;1m File Size: \u001b[0m", os.path.getsize('rsa_chunks\\wordlist1.txt'), u"\u001b[32;1m bytes "
                                                                                                u"\u001b[0m")
    print(u"\u001b[32;1m Time for 512-bit key: \u001b[0m", end - start, u"\u001b[32;1m seconds \u001b[0m")

with open('rsa_chunks\\wordlist2.txt', 'rb') as f:
    message = f.read()
    # Start timer
    start = time.perf_counter()
    for chunk in iter(lambda: f.read(512), b''):
        # Encrypt chunk
        crypto = rsa.encrypt(chunk, publicKey)
        print(crypto)
    # End timer
    end = time.perf_counter()
    f.close()
    print(u"\u001b[32;1m File Size: \u001b[0m", os.path.getsize('rsa_chunks\\wordlist2.txt'), u"\u001b[32;1m bytes "
                                                                                                u"\u001b[0m")
    print(u"\u001b[32;1m Time for 512-bit key: \u001b[0m", end - start, u"\u001b[32;1m seconds \u001b[0m")

with open('rsa_chunks\\VC_redist.x64.exe', 'rb') as f:
    message = f.read()
    # Start timer
    start = time.perf_counter()
    for chunk in iter(lambda: f.read(512), b''):
        # Encrypt chunk
        crypto = rsa.encrypt(chunk, publicKey)
        print(crypto)
    # End timer
    end = time.perf_counter()
    f.close()
    print(u"\u001b[32;1m File Size: \u001b[0m", os.path.getsize('rsa_chunks\\VC_redist.x64.exe'), u"\u001b[32;1m bytes "
                                                                                                u"\u001b[0m")
    print(u"\u001b[32;1m Time for 512-bit key: \u001b[0m", end - start, u"\u001b[32;1m seconds \u001b[0m")

(publicKey, privateKey) = rsa.newkeys(1024)
with open('rsa_chunks\\wordlist1.txt', 'rb') as f:
    message = f.read()
    # Start timer
    start = time.perf_counter()
    # Read file in 512 bit chunks
    for chunk in iter(lambda: f.read(1024), b''):
        # Encrypt chunk
        crypto = rsa.encrypt(chunk, publicKey)
        print(crypto)
    # End timer
    end = time.perf_counter()
    f.close()
    print(u"\u001b[32;1m File Size: \u001b[0m", os.path.getsize('rsa_chunks\\wordlist1.txt'), u"\u001b[32;1m bytes "
                                                                                                u"\u001b[0m")
    print(u"\u001b[32;1m Time for 1024-bit key: \u001b[0m", end - start, u"\u001b[32;1m seconds \u001b[0m")

with open('rsa_chunks\\wordlist2.txt', 'rb') as f:
    message = f.read()
    # Start timer
    start = time.perf_counter()
    for chunk in iter(lambda: f.read(1024), b''):
        # Encrypt chunk
        crypto = rsa.encrypt(chunk, publicKey)
        print(crypto)
    # End timer
    end = time.perf_counter()
    f.close()
    print(u"\u001b[32;1m File Size: \u001b[0m", os.path.getsize('rsa_chunks\\wordlist2.txt'), u"\u001b[32;1m bytes "
                                                                                                u"\u001b[0m")
    print(u"\u001b[32;1m Time for 1024-bit key: \u001b[0m", end - start, u"\u001b[32;1m seconds \u001b[0m")

with open('rsa_chunks\\VC_redist.x64.exe', 'rb') as f:
    message = f.read()
    # Start timer
    start = time.perf_counter()
    for chunk in iter(lambda: f.read(1024), b''):
        # Encrypt chunk
        crypto = rsa.encrypt(chunk, publicKey)
        print(crypto)
    # End timer
    end = time.perf_counter()
    f.close()
    print(u"\u001b[32;1m File Size: \u001b[0m", os.path.getsize('rsa_chunks\\VC_redist.x64.exe'), u"\u001b[32;1m bytes "
                                                                                                u"\u001b[0m")
    print(u"\u001b[32;1m Time for 1024-bit key: \u001b[0m", end - start, u"\u001b[32;1m seconds \u001b[0m")

(publicKey, privateKey) = rsa.newkeys(2048)
with open('rsa_chunks\\wordlist1.txt', 'rb') as f:
    message = f.read()
    # Start timer
    start = time.perf_counter()
    # Read file in 512 bit chunks
    for chunk in iter(lambda: f.read(2048), b''):
        # Encrypt chunk
        crypto = rsa.encrypt(chunk, publicKey)
        print(crypto)
    # End timer
    end = time.perf_counter()
    f.close()
    print(u"\u001b[32;1m File Size: \u001b[0m", os.path.getsize('rsa_chunks\\wordlist1.txt'), u"\u001b[32;1m bytes "
                                                                                                u"\u001b[0m")
    print(u"\u001b[32;1m Time for 2048-bit key: \u001b[0m", end - start, u"\u001b[32;1m seconds \u001b[0m")

with open('rsa_chunks\\wordlist2.txt', 'rb') as f:
    message = f.read()
    # Start timer
    start = time.perf_counter()
    for chunk in iter(lambda: f.read(2048), b''):
        # Encrypt chunk
        crypto = rsa.encrypt(chunk, publicKey)
        print(crypto)
    # End timer
    end = time.perf_counter()
    f.close()
    print(u"\u001b[32;1m File Size: \u001b[0m", os.path.getsize('rsa_chunks\\wordlist2.txt'), u"\u001b[32;1m bytes "
                                                                                                u"\u001b[0m")
    print(u"\u001b[32;1m Time for 2048-bit key: \u001b[0m", end - start, u"\u001b[32;1m seconds \u001b[0m")

with open('rsa_chunks\\VC_redist.x64.exe', 'rb') as f:
    message = f.read()
    # Start timer
    start = time.perf_counter()
    for chunk in iter(lambda: f.read(2048), b''):
        # Encrypt chunk
        crypto = rsa.encrypt(chunk, publicKey)
        print(crypto)
    # End timer
    end = time.perf_counter()
    f.close()
    print(u"\u001b[32;1m File Size: \u001b[0m", os.path.getsize('rsa_chunks\\VC_redist.x64.exe'), u"\u001b[32;1m bytes "
                                                                                                u"\u001b[0m")
    print(u"\u001b[32;1m Time for 2048-bit key: \u001b[0m", end - start, u"\u001b[32;1m seconds \u001b[0m")
