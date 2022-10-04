# import modules random and string
import random
import string

def random_dicts():
    j = 1
    thisdict = {}
    number_of_keys = random.randint(1, 28)
    while j <= number_of_keys:
        thisdict.update({random.choice(string.ascii_lowercase): random.randint(0, 100)})
        j = j + 1
    return(thisdict)

def keys_list():
    n = 0
    list_of_keys = []                                                           # create empty list
    while n < len(list_of_dicts):                                               # check if variable less than length (not including end, because already started from 0)
        for k in list_of_dicts[n].keys():                                       # take every key one by one
            if k not in list_of_keys:                                           # check if key is not exists in list of keys
                list_of_keys.append(k)                                          # if not, add to the list
        n = n + 1                                                               # increase variable to check next dict
    return list_of_keys

def dict_sum():
    new_dict = {}                                                               # create new dict for result
    for keys in keys_list():                                                    # checking all keys one by one
        """checking every dict one by one
        if current key exists in current dict, add it to the list of values
        if not exists, add value -999 (to save correct index of dict)"""
        list_of_values = [value.get(keys, -999) for value in list_of_dicts]
        max_value = max(list_of_values)                                         # find max value for current key
        max_index = list_of_values.index(max_value) + 1                         # find index for it, +1 - because start position is 0

        if len([i for i in list_of_values if i > 0]) > 1:                       # count all values greater than 0
            temp_key = keys + '_' + str(max_index)                              # if current key exists in more, than 1 dict, add number of initial dict to the name of current key
        else:
            temp_key = keys                                                     # if not, no need to add number of initial dict

        new_dict.update({temp_key: max_value})                                  # add current key and max value to the new dict
    return new_dict


list_of_dicts = []
for i in range(random.randint(2, 10)):
    list_of_dicts.append(random_dicts())
print('------------------------------')
print('Random dicts list generated:', list_of_dicts)
print('------------------------------')
print('New dictionary is:', dict_sum())
print('------------------------------')
