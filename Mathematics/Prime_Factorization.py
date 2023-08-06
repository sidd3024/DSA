# Naive Approach-->



def prime_factors_check(n):
    temp,i=n,2
    l=[]
    if n==1:
        pass
    else:
        while(i<=n):
            if temp%i==0:
                l.append(i)
                temp=temp//i
                continue
            elif temp==1:
                break
            else:
                i=i+1
        return l


print("Prime factors of given nos are :",prime_factors_check(20))


#Time Complexity--> worst case --> O(n), in case of perfect squares/cubes--> O(logn)

#Space Complexity --> O(k)--> where k is no of prime factors in case of a prime no k=1 so O(1)