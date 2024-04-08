# garbage collection
# referene count

# 문자열 객체를 변수 my_name이 참조했다
# 레퍼런스 카운트가 1인 상태
my_name = "국희"

# 레퍼런스 카운트가 2인 상태
your_name = my_name

# 레퍼런스 카운트가 하나씩 줄어서 0이 된다
my_name = 1
your_name = 2

# '국희'의 레퍼런스 카운트가 0 -> garbage collection에 의해 메모리상의 제거 대상으로 인식
