#######################################################
#program: binary_search.py
#author: Crass93
#version: 1.0
#date: 10.01 2022
#description: Search more effectively using a binary search algorythm! 
#######################################################

import random
import time      #we import this to test our search fucntions speed

def naive_search(l, target):
    """
    this is the naive search function against which we will compare our binary search,
    its basicaly a bruteforce search solution which scans entire list (l) and checks if target is in the list, if yes return the index,
    if no, then return -1 (return -1 means program is returning an error or anomaly)

    arguments:
    l: a sorted list of numbers
    target: a number we are searching for
    """
    for i in range(len(l)):
        #lets say we search for 5
        #example list = [1, 3, 5, 8, 12]
        if l[i] == target:     #if our target(5) is in our list(l) return index of taret(5) which is in this case 2(third index starting from 0)
            return i
    print(f"target {target} not found in a list")    
    return -1
    
def binary_search(l, target, low=None, high=None):
    """
    binary search takes advantage of the fact that the list (l) is sorted, basicaly, it defines a midpoint,
    and then uses that midpoint to determine if target is bigger or smaller than that midpoint,
    which narrows down the search.

    arguments:
    l: a sorted list of numbers
    target: a number we are searching for
    keyword arguments:
    low: lowest possible index in list we will search from, defaults to 0
    high: highest possible index in list we will search from, defaults to length of list - 1
    """
    if low is None:       #we want the lowest possible index that we can  check, so if low is not defined,
        low = 0           #it defaults to lowest possible index
    if high is None:
        high = len(l) -1  `#high defaults to the number of elements -1 because number of elements is counted from 1 but indexing begins with 0`
    
    if high < low:                                           #this code checks if target is in the list, the only time high is smaller than low is
        print(f"target {target} not found in a list")        #if target isnt in the list
        return -1
    
    midpoint = (low + high) // 2    #double division sign (//) calls floor division built in fucntion, floor division basicaly rounds down if number is decimal
                                    #for example 5 / 2 equals 2.5, 5 // 2 equals 2, used because midpoint index cannot be decimal number
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)   #basicaly, returns an updated binary_search fucntion where high default value is now the value of midpoint -1
    else:
        #in other words target > l(midpoint)
        return binary_search(l, target, midpoint+1, high)  #returns an updated binary_search fucntion where low default value is n0w the value of midpoint +1

if __name__ == "__main__":
    # comment out the code to test if fucntions work
    # l = [1, 3, 5, 8, 12]
    # target = 5
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    #so, if both functions do the job, why use the binary search? lets demonstrate this on a long a$$ list of numbers

    length = 50000

    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("naive_search timespan: ", (end - start), "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("binary_search timespan: ", (end - start), "seconds")

    #WOW, thats quite a difference! you can see now why its a good idea to use binary search, especially with long lists.
