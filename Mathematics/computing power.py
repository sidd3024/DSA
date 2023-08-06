# Naive approach -->
import math


def power(x,n):
    res=1
    for i in range(n):
        res*=x
    return res


# Time Complexity --> O(n)
#Space Complexity --> O(1)





# Efficient approach --



def power_eff(x,n):
    if n%2==0:
        res = 1
        for i in range(n//2):
            res*=x
        return res*res
    else:
      return power_eff(x,n-1)*x

# or

# def power_a(x,n):
#     if n==0:
#       return 1
#     temp=power_a(x,n//2)
#     temp*=temp
#     if (n%2==0):
#         return temp
#     else:
#         return temp*x
#
# # print(power_eff(3,71))
#
#
# print(power_a(3,7))


#Time Complexity --> O(log(n))
#Space Complexity --> O(log(n))


#Most Efficient -> Iterative power(Binary explanation)-->


def bin_iterative_power(n,x):
    res=1
    idx=0
    while(x>0):
        if x%2!=0:
            if idx==0:
                temp=res*n
            else:
                temp=temp*temp
            res=res*temp
            idx+=1
        else:
            if idx==0:
                temp=res*n
            else:
                temp=temp*temp
            idx+=1
        x=x//2
    return res



print(bin_iterative_power(4,5))
print(math.pow(4,5))