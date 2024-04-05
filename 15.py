# thread 동기화 테스트
from threading import Thread
from multiprocessing import Value, Lock

# Value: 공유자원 생성자


def counter1(snum, cnt, lock):
    lock.acquire()  # lock을 건다
    try:
        # snum: shared number(object), cnt: count
        for i in range(cnt):
            snum.value += 1
    finally:
        lock.release()  # lock을 해제한다


def counter2(snum, cnt, lock):
    lock.acquire()
    try:
        # snum: shared number(object), cnt: count
        for i in range(cnt):
            snum.value -= 1
    finally:
        lock.release()


if __name__ == "__main__":

    lock = Lock()
    shared_num = Value("i", 0)  # integer타입, 초기값 0의 공유자원 만든다
    t1 = Thread(target=counter1, args=(shared_num, 10000, lock))
    t1.start()

    t2 = Thread(target=counter2, args=(shared_num, 10000, lock))
    t2.start()

    t1.join()  # join(): 호출된 프로세스 종료될때까지 block된다
    t2.join()

    print("finally, number is : ", shared_num.value)
    # -34가 출력된: 즉, 공유자원에 두 개의 프로세스가 동시에 접근하여
    # 연산하면서 연산된 값이 0 이 아니라 -34로 나온 것
