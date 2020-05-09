import random
import numpy as np 
import sys

height = int(input('please input height:'))

def sumre(nums,count = 0):
    # print(nums)
    if len(nums) == 0:
      return 0
    try:
        if count == len(nums):
            return sum(nums)

        elif nums[count] == 13:
            try:
                nums = nums[:count] + nums[count+2:]
            except IndexError:
                nums = nums[:count] + nums[count+1:]
            count += 1
            return sumre(nums,count)
        else:
            count += 1
            return sumre(nums,count)
    except IndexError:
        if 13 not in nums:
            return sum(nums)
        else:
            nums = nums[:nums.index(13)] + nums[nums.index(13)+1:]
            return sum(nums)
    # print(nums)


print(sumre([13,0,13]))

def reverse_pyramid(height,count = height):

    print(' ' * (height-count) + "#" *  (count*2) )

    if count == 0:
        print('it is done')
    else:
        count -= 1
        return reverse_pyramid(height,count)
        
      
def pyramid(height,count = 0):
    
    print(' ' * (height - count) + '#' * (count*2) )

    if count == height:
        return reverse_pyramid(height,height)
 
    else:
        count += 1
        return pyramid(height,count)

pyramid(height)



def sum67(nums):
    record = True
    total = 0

    for n in nums:
        if n == 6:
            record = False

        if record:
            total += n
            continue

        if n == 7:
            record = True

    return total
    
def sum13(nums):

    total = 0
    i = 0

    while i < len(nums):
        if nums[i] == 13:
            i += 2
            continue
        total += nums[i]
        i += 1

    return total

def last2(str):
    count= 0
    for i in range(len(str)):
        if str[i:i+1] == str[-2:]:
            # print(str[i:i+2])
            print(str[-2:])
            count += 1
    return count

print(last2('hixxhi'))

def has22(nums):
    print(nums)
   
    for i in range(len(nums)-1):  
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False
        
  

# print(has22([random.randrange(1,3) for i in range(3)]))

def no_teen_sum(a, b, c):

    
    def fix_teen(n):
        
        if  n != 15 and n != 16 and n in range(13,20):
            n = 0
    
         
        return n
    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)
  
  
    return sum([a,b,c])

# print(no_teen_sum(15,16,18))

def Chocolate(small,big,goal,count = 0):

    if big > 0 and 5 <= goal:
        goal = goal - 5
        big -= 1
        return Chocolate(small,big,goal,count)
    elif small >= goal and goal > 0:
        small -= 1
        goal -= 1
        count += 1
        return Chocolate(small,big,goal,count)
    elif small < goal:
        return -1
    return count

# print(Chocolate(6,2,7))

def make_chocolate(small, big, goal,count = 0):
    if goal >= 5 * big:
        remainder = goal - 5 * big
    else:
        remainder = goal % 5
        
    if remainder <= small:
        return remainder
        
    return -1


def lucky_sum(a, b, c):
  lst = [a,b,c]
  for i in range(len(lst)):
    if lst[i] == 13:
      try:
        del lst[i]
        del lst[i+1]
      except IndexError:
        del lst[i]
  return sum(lst)
