#
# #Naive approach -
# def greatest_common_divisor(a,b):
#     r=min(a,b)
#     # print(r)
#     if (a%r==0) and (b%r==0):
#         return r
#     else:
#         i=1
#         while(i<r):
#             # print(i)
#             if(a%i==0) and (b%i==0):
#                 gcd=i
#             else:
#                 pass
#             i += 1
#         return gcd
#
# print("Greatest common divisor between two given nos are :",greatest_common_divisor(25,1001))



# Time complexity--> O(min(a,b))
#Space complexity--> O(1)


# Optimized approach -

# Problem with above is that if we have very large two nos such as a =100000000000 and b=9999999
# then we have to run for 9999999 times which can be optimized and not good for very large nos , hence
# we can use "Eucliedeans algorithim" for finding gcd


#Eucliedean's Algorithim -

# Please read the notes for the detailed imlementation



def greatest_common_divisor(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    else:
        if a>b:
            return greatest_common_divisor(a%b,b)
        else:
            return greatest_common_divisor(a,b%a)


print("Greatest common divisor between two given nos are :",greatest_common_divisor(25,1000))

# Time Complexity --> O(log(min(a,b))
#Space Complexity --> 0(log(min(a,b))