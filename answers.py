print("------------------- Question 1 ----------------")
print("This function takes a list and returns True if the items in the list are continually increasing, and False if they are not.")

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

print("This function takes a list of single digit numbers and converts it into a single integer.")

def NumConvert(list):
  string_to_int = [str(num) for num in list]
#Convert each integer to a string
  total = "".join(string_to_int)
#Combine each string with a comma
  return int(total)


print("The list [3,5,1] becomes" , NumConvert([3,5,1]))
print("The list [7,7,7,7,7,7,7] becomes" , NumConvert([7,7,7,7,7,7,7]))
print("The list [8,1,0,1,8] becomes" , NumConvert([8,1,0,1,8]))


print("------------------- Question 3 ----------------")
print("This function takes a string representing a binary number and returns an integer of that number converted into a decimal.")


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