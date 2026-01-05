#무한 반복문을 이용한 업다운 게임

import random
count=0#정답을 맞출때까지 도전 횟수 데이터를 저장할 변수 count
number=random.randint(1,100)#1-100중 무작위로 뽑은 수

while True:
    answer=int(input("1부터 100까지 중 하나의 수를 골랐습니다. 무엇인지 맞춰보세요!"))
    count+=1

    if answer==number:
        print("정답입니다!")
        print(str(count)+"번 만에 정답을 맞췄습니다.")
        break

    elif answer<number:
        print("업")

    else:
        print("다운")

