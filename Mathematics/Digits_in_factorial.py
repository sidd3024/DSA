import math as m
class Solution:
    def digitsInFactorial(self,N):
        # code here
        res=1
        for i in range(1,N+1):
            res+=m.log10(i)
        return int(res)

#Optimizd code above


#Time Complexity--> O(n)
#Space Complexity--> O(1)