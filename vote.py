votes=['짜장', '짬뽕', '짜장', '볶음밥', '짜장', '짬뽕']

count={}
for menu in ['짜장','짬뽕','볶음밥']:
    count[menu]=0
for v in votes:
    count[v] += 1

print(count)
print(count['짜장'], sum(count.values()))

count = {'짜장': 3, '짬뽕': 2, '볶음밥': 1, '탕수육': 4}
def second(x): # 튜플 x를 받아 두 번째 값(횟수)을 돌려줌
    return x[1]

print(list(count.items()))
print(sorted(count.items())) 
print(second(('짜장', 3))) # 3
a = sorted(count.items(), key=second, reverse=True) # 일반 함수
b = sorted(count.items(), key=lambda x: x[1], reverse=True) # 람다
print(a)
print(b)