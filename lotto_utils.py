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

COLS = ['당첨번호1', '당첨번호2', '당첨번호3', '당첨번호4', '당첨번호5', '당첨번호6']

def load_counts(fname):

    df = pd.read_csv(fname, encoding='utf-8-sig')
    count = {}
    for n in range(1, 46):
        count[n] = 0
    for col in COLS:
        for n in df[col]:
            count[n] += 1
    return count

def top_numbers(count,top=20):
    items = sorted(count.items(),key=lambda x:x[1],reverse=True)
    nums = []
    for n,c in items[:top]:
        nums.append(n)
    return nums

def make_hot_game(count):
    return sorted(random.sample(top_numbers(count),6))

def fill_game(picked):
    rest=[]
    for n in range(1,46):
        if n not in picked:
            rest.append(n)
    game = list(picked) + random.sample(rest, 6 - len(picked))
    return sorted(game)
        