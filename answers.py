print("------------------- Question 1 ----------------")
print("this function takes a list and returns True if the items in the list are continually increasing, and False if they are not")

def isIncreasing(list):
  for item in range(len(list)):
    if list[item] >= list[item + 1]:
      return "False"
    elif list[item] < list[item + 1]:
      return "True"

print("The list [1,2,3,4,5] is continually increasing." , isIncreasing([1,2,3,4,5]))
print("The list [6,2,11,4,5] is continually increasing." , isIncreasing([6,2,11,4,5]))
print("The list [2,4,6,8,10] is continually increasing." , isIncreasing([2,4,6,8,10]))







#2 - NumConvert (20pts)

#Write a function named *NumConvert*. It should take a list of single
#digit numbers and convert it to an integer and return it.

#For example NumConvert([3,5,1]) would return the number 351.

#Assume all items in the list are positive single digits.

#If you are totally stuck on this, DM me on Zulip and I will provide a
#hint but you won't be able to get full credit if you take the hint.

print("------------------- Question 2 ----------------")

def NumConvert(list):
  str = ""
  for num in range(len(list)):
    str += num
  return (str)
  
print(NumConvert([3,5,1]))




print("------------------- Question 3 ----------------")
print("this function takes a string representing a binary number and returns an integer of that number converted into a decimal.")


def BinConvert(bin):
  place = 0
  result = 0
  for char in bin[::-1]:
    if char == '1':
      result += 2**place
      place += 1
    elif char == '0':
      place += 1
  return result

print ("1011 is converted into" , BinConvert('1011'))
print ("101 is converted into" , BinConvert('101'))
print ("10 is converted into" , BinConvert('10'))
print ("1 is converted into" , BinConvert('1'))