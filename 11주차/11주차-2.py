height = float(input("키를 입력하세요"))
weight = float(input("몸무게를 입력하세요"))

height = height / 100
bmi = weight / (height*height)

print("당신의 BMI 는 %d입니다" % bmi)


name = "hi"
num = 1
float_num = 1.0
print("%s %d %f" % (name, num, float_num))
