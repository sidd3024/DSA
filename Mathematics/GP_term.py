import math


def termOfGP(A, B, N):
    # Your code
    if N == 1:
        return A
    elif N == 2:
        return B
    else:
        r = B / A
        nterm = math.floor(A * math.pow(r, N - 1))
    return nterm


print(termOfGP(-27,-78,3))


#Time Complexity --> O(1)
#Space Complexity --> O(1)