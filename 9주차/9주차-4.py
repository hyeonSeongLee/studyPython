i=0
dan=0

dan=int(input("출력할 구구단 단을 입력하세요."))
for i in range(1,10) :
    print("%d x %d = %d" % (dan, i, (dan*i)))
