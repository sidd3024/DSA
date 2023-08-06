

# #Brute force approach -
# def trailing_zeros_fact(n,num_calls=0):
#      count=0
#      if n==0:
#          return 1
#      else:
#          num_calls+=1
#          k=n*trailing_zeros_fact(n-1,num_calls)
#          if num_calls==1:
#              while(k%10==0):
#                  count+=1
#                  k=k//10
#              return count
#          else:
#              return k
#
#
#
#
# print("No of trailing zeros in the factorial of given no is :",trailing_zeros_fact(10))


# problem - with the above approach as the no increases so does the time taken to do multiplication and division we cant consider those operations to be O(1)
# and also using recurssion for solving for a large no is also not fesiable


#Optimized approach -
#1) since pair of (2,5) will lead to no of trailing spaces ie no of (2,5) pair=no of trailing zeros
# hence we have to find the no of (2,5) in that numbers factorial so what we can do is we can find how many 2,5 prime factors are there for that factorial
# ex- 10 ! = 1*2*3*4*5*6*7*8*9*10(2*5) ie no of (2,5) pair is 1 hence num trailing zeros =1
# with this logic we can see that at every 5th position we will have a 5 ex - 5,10,15,20 if n=20 , if we break this no of (2,5) pair will be 4 as we will be breaking 15 into 5*3 , and 20 into 5*2*2
# also how many 5 is there equal no or more no of 2 will be here so counting no of 5 will give us euaivalent no of (2,5) pair
# in case of 25 prime factors of 25 will be 5*5 ie 2 5's are there so in this case we have to consider that at every 25th step we will be having two 5,s
# hence formula comes as if n<10 : no of 5= n/5 if n>=25 then no of 5 = n//5+n//25 , if n>=125 then  n//5+n//25+n//125...

# code -


def trailing_zeros(n):
    temp=n
    count=1
    num=0
    while(temp>=5):
        num=num+n//5**count
        count+=1
        temp=temp//5
    return num

print("No of trailing zeros are :",trailing_zeros(25))


# Time complexity-

# O(log(n))--> base 5

#Space Complexity-
# O(1)