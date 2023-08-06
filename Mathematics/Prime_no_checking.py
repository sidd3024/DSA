#Naive approach -->

# def isPrime(n):
#     if n==1:
#         return True
#     else:
#         for i in range(2,n):
#             if (n%i==0):
#                 return False
#         return True

# This approach wil tell if a given no is a prime no or not

#Time Complexity --> O(n-2)==> O(n)

# Can we think of a better solution than this which can reduce the time complexity:

#Efficient approach


def isPrime(n):
    if n == 2 or n == 3:
        return True
    elif n==1:
        return True
    elif n%2==0 or n%3==0:
        return False

    i=5
    while(i*i<=n):
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True

print("Given no is a prime no:",isPrime(121))


#Time complexity --> O(sqrt(n)//3=-> O(sqrt(n))
#Space complexity--> O(1)