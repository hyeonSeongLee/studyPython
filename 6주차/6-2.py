#==============
#농부 NPC 프로그램
#=================

#상태정의 (휴식, 벌목, 목재판매)

status = "휴식"

status = input("현재 NPC 상태를 입력하세요 (휴식/벌목/목재판)")
time = int(input("현재 시간을 입력하세요"))

#print(status)
#print(time)

#for 문을 통한 자동화
for i in range (3) :

    status = input("현재 NPC 상태를 입력하세요 (휴식/벌목/목재판)")
    time = int(input("현재 시간을 입력하세요"))

    if status == "휴식" :
        if time >= 9 :
            status = "벌목"
            print(status)

    elif status == "벌목" :
        if time >= 17 :
            status = "목재판매"
            print(status)

    elif status == "목재판매" :
        if time >= 19 :
            status = "휴식"
            print(status)
