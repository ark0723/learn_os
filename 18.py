foods = ["김치찌개", "곱창전골", "족발", "양념치킨"]

print(id(foods))  # id() : 메모리 주소 # 실행할때마다 랜덤한 주소로 나옴(RAM)
print(hex(id(foods)))  # hex: 메모리 주소를 16진수로 표현

# memoryview object
mv = memoryview(b"happy day")  # b'': 문자열을 byte 형태로 저장하겠다
print(mv)

print(mv[0])  # h : unicode가 출력된다
print(mv[1])  # a
print(mv[2])  # p mv[2]와 mv[3]는 동일한 곳을 가리킨다
print(mv[3])  # p
