# import module random
import random
# generate random list
random_list = random.sample(range(0, 1001), 100)
# print random list
print('Random range: ', random_list)

# assign beginning value 0 to the variable for first cycle
j = 0
# compare every two consequent elements of the list from first pair till last pair one by one j times
# during this cycle biggest element takes last position in the list
# j depends on list length
while j < len(random_list)-1:
  # assign beginning value 0 to the variable for second (small) cycle
  i = 0
  # compare every two consequent elements of the list from first pair till last pair
  # number of last pair depends on list length
  # -1 because i is position of first element in the pair, can't compare last element with nothing
  # -j because every j cycle biggest elements takes last position in cycle, no need to compare sorted part again
  while i < len(random_list)-1-j:
    # compare two consequent elements
    if random_list[i] > random_list[i+1]:
      # if previous element bigger than next one, swap it
      random_list[i], random_list[i+1] = random_list[i+1], random_list[i]
    # to compare next pair increase index i
    i = i + 1
  # check all pairs one by one from the beginning
  j = j + 1

print('Sorted list: ', random_list)

# create empty list for even numbers
even = list()
# create empty list for odd numbers
odd = list()

# check every element in the list
for k in random_list:
  # if it can be devided by 2, add it to list of even numbers
  if k % 2 == 0:
    even.append(k)
  # if it can't be devided by 2, add it to list of odd numbers
  else:
    odd.append(k)
# print('even_list = ', even)
# print('odd_list = ', odd)

# check length of even list
if len(even) > 0:
  # if it is not 0, print AVG value
  print('AVG value of even numbers is ', sum(even)/len(even))
  # if it is 0, print warning message
else:
  print('There are no even numbers in the list')

# same for odd list
# check length of odd list
if len(odd) > 0:
  print('AVG value of odd numbers is ', sum(odd)/len(odd))
# if it is 0, print warning message
else:
  print('There are no odd numbers in the list')


############################
# I was trying to concatenate two last blocks in one cycle, but did not find, how to print name of list in warning message yet
# avg_list = [even, odd]
# print('avg_list = ', avg_list)
#
# for l in avg_list:
#   print('list ',l)
#   if len(l) > 0:
#     print(l, len(l))
#     print('AVG value of NAME numbers is ', sum(l)/len(l))
#   else:
#     print('There are no NAME numbers in the list')
