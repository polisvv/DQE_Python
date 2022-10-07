# import modules random and string
import random
import string

def generate_random_dicts(dict_num_min,
                          dict_num_max,
                          key_num_min,
                          key_num_max,
                          value_min,
                          value_max):
    global list_of_dicts
    list_of_dicts = []
    for i in range(random.randint(dict_num_min, dict_num_max)):
        j = 1
        thisdict = {}
        number_of_keys = random.randint(key_num_min, key_num_max)
        while j <= number_of_keys:
            thisdict.update({random.choice(string.ascii_lowercase): random.randint(value_min, value_max)})
            j = j + 1
        list_of_dicts.append(thisdict)


    return list_of_dicts

def get_keys_list(dicts):
    n = 0
    list_of_keys = []                                                           # create empty list
    while n < len(dicts):                                                       # check if variable less than length (not including end, because already started from 0)
        for k in dicts[n].keys():                                               # take every key one by one
            if k not in list_of_keys:                                           # check if key is not exists in list of keys
                list_of_keys.append(k)                                          # if not, add to the list
        n = n + 1                                                               # increase variable to check next dict
    return list_of_keys

def dict_sum(dict):
    new_dict = {}                                                               # create new dict for result
    for key in get_keys_list(list_of_dicts):                                                    # checking all keys one by one
        """checking every dict one by one
        if current key exists in current dict, add it to the list of values
        if not exists, add value -999 (to save correct index of dict)"""
        list_of_values = [value.get(key, -999) for value in dict]
        max_value = max(list_of_values)                                         # find max value for current key
        max_index = list_of_values.index(max_value) + 1                         # find index for it, +1 - because start position is 0

        if len([i for i in list_of_values if i > 0]) > 1:                       # count all values greater than 0
            temp_key = key + '_' + str(max_index)                              # if current key exists in more, than 1 dict, add number of initial dict to the name of current key
        else:
            temp_key = key                                                     # if not, no need to add number of initial dict

        new_dict.update({temp_key: max_value})                                  # add current key and max value to the new dict
    return new_dict


random_dict = generate_random_dicts(2, 10, 1, 28, 0, 100)
print('------------------------------')
print('Random dicts list generated:', random_dict)
print('------------------------------')
print('New dictionary is:', dict_sum(random_dict))
print('------------------------------')
