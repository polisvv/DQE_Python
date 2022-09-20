# import module random
import random
# generate random list
random_list = random.sample(range(0, 1001), 100)
# print random list
print('Random range: ', random_list)
# create empty list, it will be used for ordered list of random numbers
sorted_list = list()
# create empty list for even numbers
even_list = list()
# create empty list for odd numbers
odd_list = list()

# checking if random list is not empty
while random_list:
  # if it is not empty, find minimum number and add it to the sorted list
  sorted_list.append(min(random_list))
  # check if minimum number is even
  if min(random_list) % 2 == 0:
    # if it is even, add to even list
    even_list.append(min(random_list))
  # if it is not even, add it to odd list
  else:
    odd_list.append(min(random_list))
  # delete minimum value from random list
  random_list.remove(min(random_list))
# when random_list is empty, print final resul of sorted_list
print('sorted_list = ', sorted_list)
# calculate and print AVG value of even numbers
print('AVG value of even numbers is ', sum(even_list)/len(even_list))
# skipp if there is error (dividing on zero, if there is no even numbers)
pass
# calculate and print AVG value of odd numbers
print('AVG value of odd numbers is ', sum(odd_list)/len(odd_list))
# skipp if there is error (dividing on zero, if there is no odd numbers)
pass
