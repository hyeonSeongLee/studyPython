
cart = []


#for i in range(1,4):

while True:
    
    item = input("추가하고 싶은 값을 입력하세요")

    cart.append(item)
    print(cart)

    end = int(input("그만두고 싶으면 1을 누르세요, 삭제하고 싶으면 2를 누르세요"))

    if end == 1:
        break
    elif end == 2:
        item2 = input("삭제할 아이템을 입력하세요"
                      )
        cart.remove(item2)
