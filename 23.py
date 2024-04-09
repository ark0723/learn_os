try:  # 존재하지 않는 파일을 읽으려고 하면 에러발생
    f = open("none.txt", "r")
    print(f.read())
    f.close()

except FileNotFoundError as e:
    print(e)
    # issubclass(첫째인자, 둘째인자): 첫째인자가 둘째인자의 하위 클래스가 맞는지 true/false return
    print(issubclass(FileNotFoundError, OSError))
    print(issubclass(ZeroDivisionError, OSError))
