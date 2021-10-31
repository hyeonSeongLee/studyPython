#인공생명체 파라미터 튜닝
#while 이용
#파라미터 2개의 값을 얻는다.
#공격력
#치명율
#데미지 = 공격력 * 치명율
#플레이어 HP = 2000

#================================
#랜덤 외부 함수 라이브러리 적용

from random import *

#================================
#변수 선언
enemy_attack = 20
enemy_critical = 40
player_hp = 2000

#================================
#파라미터 탐색
while (player_hp > (enemy_attack*enemy_critical)) :
    print(enemy_attack)
    print(enemy_attack * enemy_critical)

    enemy_attack = randint(1,100)
    enemy_critical = 100 - enemy_attack

    """
    enemy_attack = enemy_attack + 1
    enemy_critical = enemy_critical + 1
    """
#================================
#출력
print("공격력 : ", enemy_attack)
print("치명율 : ", enemy_critical)
print("데미지 : ", enemy_attack * enemy_critical)
