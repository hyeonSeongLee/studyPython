while True :
    a = int(input("숫자를 입력하세요 짝수면 탈출 가능"))
    if a%2 == 0 and a >0 :
        print ("짝수를 입력했습니다. break 를 통한 탈출 성공")
        break
    else :
        print ("홀수 또는 0을 입력했습니다. 탈출 실패")
