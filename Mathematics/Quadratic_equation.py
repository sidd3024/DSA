import math as m

def quadraticRoots (a, b, c):
    # code here
    try:
      x1 = (-b + m.sqrt(m.pow(b, 2) - 4 * a * c)) // (2 * a)
      x2 = (-b - m.sqrt(m.pow(b, 2) - 4 * a * c)) // (2 * a)
    except:
      return -1
    # print(x1,x2)
    if x2 > x1:
        return int(x2), int(x1)
    else:
        return int(x1), int(x2)


print(quadraticRoots(280,399,573))


#Time Complexity --> O(1)
#Space Complexity --> O(1)