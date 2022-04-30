import string
import random
arr=['H','T'] #outcomes when a single coin is tossed
#H denotes Head
#T denotes Tail
res = ''.join(random.choices(arr, k = 2))
print("Outcome of the experiment : " + str(res))
