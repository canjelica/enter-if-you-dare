
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    #iterate through list, keep track of different integers
    #if I meet an integer in my dictionary, remove it
    #else add it
    #create an empty dict
    #check dict @ i, if not there add with value 1
    #if there, remove
    
    pairs = {}
    deleted = 0

    for sock in ar:
        if sock in pairs:
            del pairs[sock]
            deleted += 1
        else:
            pairs[sock] = 1
    
    return deleted



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
