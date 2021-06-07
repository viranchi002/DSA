from collections import OrderedDict

cache_len = 3
dictionary = OrderedDict()


def cache_get(key):
    if key in dictionary:
        dictionary.move_to_end(key)
        return dictionary[key]
    else:
        return -1


def cache_put(key, value):
    if len(dictionary) == cache_len:
        dictionary.popitem(last=False)
    dictionary[key] = value
    dictionary.move_to_end(key)


if __name__ == '__main__':
    nums = [1, 5, 6, 3, 9]
    for num in nums:
        cache_put(num, num)
    # Will print -1 as it does not exist anymore
    print(cache_get(1))
    # Will print 9
    print(cache_get(9))
