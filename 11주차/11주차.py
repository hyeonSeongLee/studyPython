#피노키오 이야기 변수 / 시간 / 코의 길이 (int)

time = 0
item = False
nose = 0

while True:

    ans = input("어디로 가시겠습니까 [마을/시장]")

    if ans == "마을":
        print("이야기1")
        time += time + 1
        
    if ans == "시장":
        print("이야기2")
        time += time + 2

        print("피노키오야 학교에 갔니?")
        ans2 = int(input("학교에 갔다 왔습니다(1), 학교에 안갔다(2)"))

        if ans2 == 1 :
            nose = nose + 1
            print("피노키오는 거짓말을 했습니다")
        #item = True


        if time >= 2 and nose >= 1:
            print("이벤트 발생")
            break
