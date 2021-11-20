#헤밍웨이의 소설 노인과 바다를 줄거리로 구성한 인터렉티브 스토리텔링입니다.
#전체적인 구조는, 노인이 항구로 이동하고 -> 바다에 나가 낚시를 시작 -> 청새치를 끌어 올렸으나 -> 상어떼의 습격을 받고 -> 뼈만남은 청새치를 가져오고 마눌린에게 보여주며 이야기가 끝이 납니다.

print("그는 홀로 조각배를 타고 멕시코만류에 나가 고기를 잡는 노인이었다. 노인은 지난 84일 동안 고기를 한 마리도 잡지 못했다.")
print("85일째 되는 날 노인은 아침 일찍 일어난다.")

#첫번째 분기점. 이야기의 시작 침대 / 항구

while True :
    a = int(input("노인은 잠을 더 청하거나, 다시 항구로 나가 낚시를 시도할 수 있습니다. 번호를 입력해 노인의 행동을 선택하세요. [1] 침대/ [2] 항구"))
    if a == 1 :
        print ("노인이 한숨 더 자는 사이 배 도둑이 노인의 배를 훔쳤습니다. 처음 선택지로 돌아갑니다")
        
    else :
        print ("노인은 항구에 도착해 항구의 소년인 마눌린을 만납니다.")
        break

print("마눌린 : 오늘은 꼭 월척을 낚을 수 있을 거에요! 조심히 다녀오세요")

#두번째 분기점. 마눌린과의 대화

while True :
    a = int(input("번호를 입력해 노인의 대답을 선택하세요. [1] 응원해줘서 고맙다 :) 출항할 수 있도록 닻을 올려주려무나/ [2] 닥쳐 애송아 :( 이번에도 못잡으면 85일째라고."))
    if a == 1 :
        print ("마눌린의 도움으로 닻이 올라가고 노인의 조각배는 멕시코만을 향해 출항합니다.")
        break 
    else :
        print ("마눌린 : 예, 그럼 85일째 굶어 보시죠. 말이 너무 심하신걸요 :( ")

while True :
    a = int(input("닻이 올라가고 노인의 조각배는 맥시코만을 향한다. 계속 진행하려면 [1]을 누르세요."))
    if a == 1 :
        break

#for i를 이용한 자동 스토리텔링

for i in range (1,15) :
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    if i == 3:
        print("항구는 점점 멀어지고, 손을 흔드는 마눌린도 더이상 보이지 않는다.")

    if i == 6:
        print("이제 노인은 바다에 혼자 남겨진다.")

    if i == 9:
        print("잔잔한 바다 위를 하늘을 나는 갈매기들이 보인다.")

    if i == 12:
        print("어느새 멀어진 육지 위로 구름이 피어오른다.")

    if i == 15:
        print("이제 슬슬 낚시를 시작해봐야겠군.")
        break

while True :
    a = int(input("노인은 미끼를 던지고 본격적인 낚시를 시작한다. 계속 진행하려면 [1]을 누르세요."))
    if a == 1 :
        break

#for 반복문과 변수의 대입을 통한 미끼와 노인과의 거리 

bate=0
striped_marlin=0
temptation = False

for i in range (1,101) :

    if temptation == False:
        striped_marlin = striped_marlin + 2


        bate = bate + 1
        print("정체불명의 물고기와 미끼와의 거리:", striped_marlin - bate)

    if (striped_marlin - bate) > 20:
        print("음 미끼가 별로인가?")
        while True :
            a = int(input("지렁이 미끼를 거두고 점심으로 남겨놓았던 오징어를 미끼로 쓰려고 한다. [1] 그래 맛있는 걸 미끼로 해야 잡히지. [2] 어휴 까다롭긴, 그냥 다른걸 잡고 만다."))
            if a == 1 :
                break
            if a == 2 :
                print("결국 노인은 85일째에도 아무런 물고기를 잡지 못하였다. 이전 선택지로 이동합니다.")
        print("바뀐 오징어 미끼를 던진지", i-20,"초밖에 안되었는데 입질이 온다.")
        temptation = True

    if  i > 20 :
        break

print("무언가가 미끼를 물었다.")
        
while True :
    a = int(input("엄청나게 힘세고 큰 정체불명의 물고기이다. 마음을 다잡고 물고기와 싸우기 시작하려면 [1]을 누르세요. 혹은 [2]을 눌러 포기하세요."))
    if a == 1 :
        break
    if a == 2 :
        print("정체불명의 물고기의 승리, 물고기는 오징어를 맛있게 먹고 도망가고, 노인은 점심을 굶은 체 항구로 돌아온다. 이전 선택지로 돌아옵니다.")

#while 반복문을 이용해 정체불명의 물고기와 노인과의 대결

striped_marlin_speed = 20
striped_marlin_strength = 40
oldman_strength = 1000

while (oldman_strength > striped_marlin_speed*striped_marlin_strength) :
    striped_marlin_speed = striped_marlin_speed + 1
    striped_marlin_strength = striped_marlin_strength + 1

    print ("정체불명 물고기의 속도 :", striped_marlin_speed)
    print ("정체불명 물고기의 힘 :", striped_marlin_strength)
    print ("정체불명 물고기가 입히는 공격력 :", striped_marlin_speed*striped_marlin_strength)
    print ("노인의 남은 체력 :", oldman_strength-striped_marlin_speed*striped_marlin_strength)

print ("생각보다 엄청난 힘의 물고기이다. 물고기를 잡기 위해서 노인은 노련한 전략을 구상해야한다.")

#if 문을 통한 정체불명의 물고기와 노인과의 대결 / 밀기 당기기 중 어느것을 눌러도 상관없으나 밀기가 조금더 빨리 끝남.

oldman_attack = 0

while True:

    ans = input("노인은 밀당을 통해 정체 불명의 물고기의 힘을 빼놓으려고 한다.[1]밀기/[2]당기기]")

    if ans == "1":
        print("노인은 낚시줄을 조금 풀어 정체불명의 물고기를 밀어낸다.")
        oldman_attack  += oldman_attack  + 1
        
    if ans == "2":
        print("노인은 낚시줄을 당겨 정체불명의 물고기를 끌어낸다.")
        oldman_attack  += oldman_attack  + 2

    if oldman_attack <= 20 :
        print("밀거나 당겨서 조금만 더 힘을 내보자!")

    if oldman_attack > 20 :
        print("노인이 전략이 먹힌 것 같다.")
        break

print ("인내 끝에 노인이 끌어올린 물고기는 지금껏 노인이 보았던 물고기 중 가장 큰 청세치였다!!")

for i in range (1,10) :
    print(" ")

    if i == 3:
        print("흡족해하는 노인은 청새치를 끌어올리고 배에 담는다.")

    if i == 6:
        print("통째로 배에 싣기에 너무 클 정도로. 85일만의 엄청난 월척이었다.")
        break

while True :
    a = int(input("노인은 청새치를 손질해서 배에 실어야 한다. 계속 진행하려면 [1]을 누르세요."))
    if a == 1 :
     break

print("이윽고 청새치의 피가 흐르면서, 불길한 기운이 든다.")

#불청객 상어 떼의 등장과, for 문을 활용한 상어와 노인의 거리 표현

shark=0
boat=30
shark_attack = False

for i in range (1,100) :

    if shark_attack == False:
        shark = shark + 2
        print("상어 떼와 노인의 보트와의 거리:", boat - shark)

    if (boat - shark) <= 0:
        print("상어 떼가 청세치의 피냄새를 맡고 찾아왔다.")
        shark_attack == True
        break

while True :
    a = int(input("상어 떼의 지느러미들이 보이기 시작한다. 계속 진행하려면 [1]을 누르세요."))
    if a == 1 :
        break

#for과 i 를 활용한 자동 스토리 텔링

for i in range (1,10) :
    print(" ")

    if i == 3:
        print("상어 떼들은 보트를 흔들어 청세치의 고기를 가로채려한다.")

    if i == 6:
        print("노인은 필사적으로 노를 휘두르며 저항하기 시작한다.")

    if i == 9:
        print("하지만 상어 떼들을 막기엔 역부족이고, 이들은 청새치를 뜯어가기 시작한다.")
        break

sharks_attack = 0
oldman_resistance = 0

#if 문을 통한 상어떼와 노인과의 대결 /어느것을 눌러도 상관없으나 결국 상어를 따돌리지 못하는 구조.

while True:

    ans = input("노인은 노를 휘둘러 상어떼를 따돌리려고 한다. [1] 노를 휘두루기 / [2] 전력으로 도망가기")

    if ans == "1" :
        print("노인은 노를 휘둘렀다.")
        oldman_resistance = oldman_resistance + 1
        print("하지만 상어의 공격은 더 거세졌다.")
        sharks_attack = sharks_attack + 2

    if ans == "2" :
        print("노인은 전속력으로 노를 저었다.")
        oldman_resistance = oldman_resistance + 1
        print("하지만 상어의 속도는 더 빨랐다.")
        sharks_attack = sharks_attack + 2

    if (sharks_attack - oldman_resistance) >= 6 :
        print("노인은 안간힘을 썼지만, 결국 상어떼를 따돌리지 못하였다.")
        break
    
#while 문을 통한 상어의 공격력과 남은 청새치 고기의 양

sharks_speed = 20
sharks_strength = 40
remain_striped_marlin_strength = 1000

while (remain_striped_marlin_strength > sharks_speed*sharks_strength) :
    sharks_speed = sharks_speed + 1
    sharks_strength = sharks_strength + 1

    print ("상어 떼의 속도 :", sharks_speed)
    print ("상어 떼의 힘 :", sharks_strength)
    print ("상어들의 공격력 :", sharks_speed*sharks_strength)
    print ("남은 청새치 고기 :", remain_striped_marlin_strength-sharks_speed*sharks_strength)

print ("결국 상어떼는 모든 청새치 고기를 먹어치우게 되었다.")

#세번째 분기. 마을로 돌아가기 와 상어들과의 혈투 중 선택. 혈투를 벌일 시 while if 문을 활용한 상어와의 전투가 실행되고, SAD ENDING 으로 끝.

while True:

    ans = input("이제 선택지는 두가지 뿐이다. [1] 마음을 비우고 항구로 돌아간다. / [2] 상어들과 혈투를 벌인다.")

    if ans == "1" :
        print("인간은 패배하도록 창조된 게 아니야. 파멸당할 수 있을지는 몰라도 패배할 수는 없어.")

        for i in range (1,15) :
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            if i == 3:
                print("육지는 점점 가까워지고, 육지 위에 노을이 피어오른다.")

            if i == 6:
                print("점처럼 보이던 항구가 점점 커진다.")

            if i == 9:
                print("잔잔한 바다 위로 하늘을 나는 갈매기들이 노인을 반긴다.")

            if i == 12:
                print("손을 흔드는 마눌린이 보이기 시작한다.")

            if i == 15:
                print("이제 도착이군.")
                break
        
        break

    if ans == "2" :
        print("노인은 전속력으로 노를 저었다.")
        oldman_resistance = oldman_resistance + 1
        print("하지만 상어의 속도는 더 빨랐다.")
        sharks_attack = sharks_attack + 2

        sharks_attack = 0
        oldman_resistance = 0

        while True:

            ans = input("분노에 휩싸인 노인은 상어떼를 도발하며 공격을 시작한다. [1] 노를 휘둘러 때리기 / [2] 청새치의 날카로운 뼈를 던지기")

            if ans == "1" :
                print("노인은 노를 휘둘러 상어들을 때렸다.")
                oldman_resistance = oldman_resistance + 1
                print("하지만 상어의 반격은 생각보다 더 거셌다.")
                sharks_attack = sharks_attack + 2

            if ans == "2" :
                print("노인은 청새치의 뼈를 던져 상어 떼를 공격하였다.")
                oldman_resistance = oldman_resistance + 1
                print("하지만 상어 떼는 조금도 물러서지 않고 반격하였다.")
                sharks_attack = sharks_attack + 2

            if (sharks_attack - oldman_resistance) >= 6 :
                print("청새치로 만족하지 못했던 상어 떼는 결국 노인마져 먹어치웠다.")
                break

        print("SAD ENDING - 마눌린은 노인을 다시 보지 못하게 되었다. 항구의 사람들이 실종된 노인을 찾으려 했으나, 그들이 마주한 것은 청새치의 뼈가 담긴 그의 조각배 뿐이었다. 자동으로 이전 선택지로 돌아갑니다.")


while True :
    a = int(input("지친 육체와 정신을 이끌고 그리고 앙상한 청새치의 뼈만 가진 체로 노인은 항구에 도착하였다. 계속 진행하려면 [1]을 누르세요."))
    if a == 1 :
        break

print("마눌린 : 할아버지, 생각보다 늦게 도착하셔서 모두 걱정하고 있었어요. 배 위에 저것은 뭔가요?")

#dictionary 자료형을 통해 조각배 안의 재고 목록 형성 및 삭제

ship_trunk = []

while True:
    
    item = ["청새치 뼈"]

    ship_trunk.append(item)
    print("재고 목록 :",ship_trunk)

    end = int(input("조각배 위엔 청새치의 뼈밖에 없는 것을 확인했습니다. 배에서 꺼내 마눌린에게 보여주려면 [1]을 입력해주세요."))

    if end == 1:
        ship_trunk.remove(item)
        print("재고 목록 :",ship_trunk)
        break

#엔딩

print("우와 제가 지금까지 본 물고기 중 가장 큰 것 같아요, 어디서 어떻게 잡은거에요? 우선은 푹 쉬고 꼭 알려주세요")
        
while True :
    a = int(input("뿌듯한 노인은 지친 몸을 이끌고 집으로 돌아가 숙면을 취하며 이야기는 끝이 납니다. 끝내려면 [1]을 입력해주세요."))
    if a == 1 :
        break
