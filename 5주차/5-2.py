a=[1,2,1,2,5,1,2,1,2,51,2,5]
b=(1,2,3)

print(b)

b[0]=10

#튜플은 이렇게 사용 불가 - 한번 선언하면 수정 불가.
#리스트의 변형, dictionary (key값을 가짐.)
# x={'a':10, 'b':20} x['a']=
"""
#하드 코딩
if a[0] == 1 and a[1] == 2 :
    print ("확인")

    if a[2] == 1 and a[3] == 2 :
        print ("invest")
"""
#===========================

#리스트 내부를 순회하며 모든 값을 비교함.
"""
for idx, i in enumerate(a) :
    #print("idx:", idx)
    #print("value:", i)

    if a[idx] ==1 and a[idx+1] ==2 :
        print("invest at:",idx)
"""
#===========================
#변수 되도록이면 상단에 선언, 다시 선언하면 안되기 때문에.

"""
a=(1,2,3)
print(a)
"""




