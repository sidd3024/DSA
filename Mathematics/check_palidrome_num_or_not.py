# Given a no you have to check if this no is palindrome or not:

num=4553 # to check if this is palindrome or not!

n=int(input("Enter a  valid number:")) 
def is_palindrome_or_not(num):
    temp=num
    rev=0
    while temp!=0:
        ld=temp%10
        rev=rev*10+ld
        temp=temp//10

    # print(rev,num)
    return rev==num


print(is_palindrome_or_not(n))