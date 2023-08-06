# Naive Approach -->
import math


# def distinct_divisor(n):
#     temp=n
#     if n==1:
#         print(1)
#     else:
#         i=1
#         while(i<=n):
#             if temp%i==0:
#                 print(i,end=" ")
#                 # temp=temp//i
#             else:
#                 pass
#             i=i+1
#



# distinct_divisor(15)



#Time Complexity---> best case O(1) ,worst_case --> O(n)
#Space Complexity--> O(1)


#Efficient Approach-->

#Thumb Rule --> Divisor of any no occurs in pair => For ex --> 30: (1,30),(2,15),(3,10),(5,6)

# Also one of the nos in the pair of these divisor should be <=sqrt(n)

# x*y, are two divisors of n

# let  x be a smaller no that y

# x<=y ie now multiplying x both sides ==> x**2<=n ie x<=sqrt(n)



def distinct_divsor_upd(n):
    i=1
    # l=[]
    while(i<=int(math.sqrt(n))):# First loop will run for sqrt(n)
        if n%i==0:
            print(i,end=" ")
            k=i
        i = i + 1

    while(k>=1):#second loop will run for sqrt(n)
        if n//k!=k and n%k==0:
            print(n//k,end=" ")
        else:
            pass

        k=k-1

    return

distinct_divsor_upd(30)



#Time Complexity--> O(sqrt(n))+O(sqrt(n))-->O(sqrt(n))

#Space Complexity O(2*k)--> k IS NO OF DIVISOR ==> O(k) if we give list otherwise if we print it will be 0(1)