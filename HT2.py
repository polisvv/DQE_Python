# import modules random and string
import random
import string

# create empty list
list_of_dicts = []

# generate random number which will be random number of dicts
number_of_dict = random.randint(2, 10)
# assign beginning value 1 to the variable for the cycle of generating dicts
i = 1
# cycle for creating generated number of dicts
# checking if variable is smaller or equal previously generated number of dicts
while i <= number_of_dict:
    # create new empty dict
    thisdict = {}
    # generate number of keys
    number_of_keys = random.randint(1, 28)
    # increase variable to 1
    i = i + 1
    # assign beginning value 1 to the variable for the cycle of generating keys and values
    j = 1
    # the cycle of generating keys and values
    # checking if variable is smaller or equal previously generated number of keys
    while j <= number_of_keys:
        # generate random key
        letter_key = random.choice(string.ascii_lowercase)
        # generate random value
        value = random.randint(0, 100)
        # update empty dict by adding generated key and value in this cycle
        # if generated key in this cycle already exists, it will be overwritten
        thisdict.update({letter_key : value})
        # increase variable to 1
        j = j + 1
    # adding generated dict to list of dicts
    list_of_dicts.append(thisdict)
print('------------------------------')
print('list_of_dicts', list_of_dicts)
print('------------------------------')


# collect all keys in one list
# assign beginning value 0 to the variable, because 1st index of list is 0
n = 0
# create empty list
list_of_keys = []
# check if variable less than length (not including end, because already started from 0)
while n < len(list_of_dicts):
    # take every key one by one
    for k in list_of_dicts[n].keys():
        # check if key is not exists in list of keys
        if k not in list_of_keys:
            # if not, add to the list
            list_of_keys.append(k)
    # increase variable to check next dict
    n = n + 1


# create new dict for result
new_dict = {}
# checking all keys one by one
for d in list_of_keys:
    # assign beginning value 0 to the variable, because 1st index of list is 0
    i = 0
    # create empty list of values for current key
    list_of_values = []
    # checking every dict one by one
    while i < len(list_of_dicts):
        # if current key exists in current dict, add it to the list of values
        # if not exists, add value -999 (to save correct index of dict)
        list_of_values.append(list_of_dicts[i].get(d,-999))
        # increase variable to go to the next dict
        i = i + 1
    # find max value for current key
    max_value = max(list_of_values)
    # find index for it
    # +1 - because start position is 0
    max_index = list_of_values.index(max_value) + 1

    # checking if current key exists in more, than 1 dict
    # count all value greate than 0
    x = [i for i in list_of_values if i > 0]
    # if current key exists in more, than 1 dict, add number of initial dict to the name of current key
    if len(x) > 1:
        temp_key = d + '_' + str(max_index)
    # if not, no need to add number of initial dict
    else:
        temp_key = d

    # add current key and max value to the new dict
    new_dict.update({temp_key : max_value})
# print result
print('------------------------------')
print('new dict is', new_dict)
print('------------------------------')
