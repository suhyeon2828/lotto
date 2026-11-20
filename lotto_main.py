from lotto_utils import *

while True:
    try:
        count = int(input("몇 게임 원해? (1~10사이 입력): "))
        if 1<= count <= 10:
            break
        print('1~10사이의 수만 입력해!!!')

    except ValueError:
        print('숫자를 입력하세요!')

games = make_games(count)
print("\n\n====로또 번호 생성기====\n\n")
for i in range(count):
    print(f"{i+1}게임 : {to_text(games[i])}")
    