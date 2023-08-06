def LCM(a,b,num_call=0):
    if a==0 :
        return b
    elif  b==0 :
        return a
    else:
        num_call+=1
        if a>b:
            l= LCM(a%b,b,num_call)
            if num_call==1:
                return (a*b)//l
            else:
                return l
        else:
            l= LCM(a,b%a,num_call)
            if num_call==1: 
                return (a*b)//l
            else:
                return l


print("LCM of the given nos are: ",LCM(7,64))



#Time Complexity--> O(log(min(a,b))+0(1)=>O(log(min(a,b))
#Space complexity-->O(log(min(a,b))