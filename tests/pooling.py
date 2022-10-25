import psutil, rsa, time

if __name__ == '__main__':

    start = time.perf_counter()
    (publicKey, privateKey) = rsa.newkeys(2048)
    end = time.perf_counter()
    print(u"\u001b[32;1m Time for 2048-bit key without pooling: \u001b[0m", end - start,
              u"\u001b[32;1m seconds \u001b[0m")

    start = time.perf_counter()
    (publicKey, privateKey) = rsa.newkeys(2048, poolsize=12)
    end = time.perf_counter()
    print(u"\u001b[32;1m Time for 2048-bit key with pooling: \u001b[0m", end - start, u"\u001b[32;1m seconds \u001b[0m")