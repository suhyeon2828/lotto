""" import random

print(random.randint(1,45))
print(random.choice([10,20,30]))
nums = [1,2,3,4,5]
r=random.shuffle(nums)
print(nums,r)
print(random.sample(range(1, 46), 6))
print(random.sample(range(1, 46), 6))

a=[33,7,21]
b=sorted(a)
print(a,b)
r = a.sort()
print(a,r)
print(sorted(a,reverse=True))

print(",".join(['사과','배','감']))
print("-".join(['2026','11','08']))

nums=[3,15,22]
strs = []
for n in nums:
    strs.append(str(n))
print(strs)
print(' - '.join(strs))
"""

import random
import pandas as pd

def make_game():
    return sorted(random.sample(range(1,46),6))

def make_games(count):
    games =[]
    for i in range(count):
        games.append(make_game())
    return games

def to_text(game):
    words = []
    for n in game:
        words.append(f'{n:3d}') #3칸 확보하고 오른쪽 정렬
    return ' '.join(words)

