import string
import random
arr=['H','T']
#outcomes when a single coin is tossed
#H denotes Head
#T denotes Tail
arr2=['1','2','3','4','5','6'] #outcomes whena a single die is rolled
res = ''.join(random.choices(arr,k = 1))
if res=='H':
    res2= ''.join(random.choices(arr,k=1))
else:
    res2= ''.join(random.choices(arr2,k=1))
print("Outcome of the experiment : "+ str(res) + str(res2))
