import threading, os, time


def something(word):
    while True:
        print(word)
        time.sleep(3)


if __name__ == "__main__":
    print("기존 프로세스 아이디 : ", os.getpid())
    thread1 = threading.Thread(target=something, args=("happy",))  # 추가 스레드 생성
    thread1.daemon = True  # 메인이 끝나면 같이 끝내겠다
    thread1.start()
    print(
        "메인 스레드에서 반복문 시작"
    )  # 파이썬 프로세스가 시작되면 default로 메인 스레드가 생성된다.
    while True:
        try:
            print("daily ...")
            time.sleep(1)
        except KeyboardInterrupt:
            print("Good Bye~")
            break
