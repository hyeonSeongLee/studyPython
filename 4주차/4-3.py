
#색 붉은색/검은색
color = None

#방향의 종류 180 / 90
dir = None

#넓이의 종류 1.5/4.0 
area = None

color = input("로스코 작품을 보고 가장 잘 드러나는 색을 입력하세요.")
dir = int(input("로스코 작품을 보고 방향을 입력하세요."))
area = float(input("로스코 작품을 보고 사각형의 대표 넓이를 입력하세요."))

if color == "붉은색" or color =="검은색" :
    if dir == 180 or dir == 90 :
        print("확인")
        if area <= 1.5 or area <= 4.0 :
            print("이것은 로스코의 작품입니다.")


        
