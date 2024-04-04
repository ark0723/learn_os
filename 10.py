from multiprocessing import Process
import os, time


def coke():
    while True:
        try:
            print("coke process id : ", os.getpid())
            print("my parent process id : ", os.getppid())
        except KeyboardInterrupt:
            break


def cider():
    while True:
        try:
            print("cider process id : ", os.getpid())
            print("my parent process id : ", os.getppid())
        except KeyboardInterrupt:
            break


def juice():
    while True:
        try:
            print("juice process id : ", os.getpid())
            print("my parent process id : ", os.getppid())
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    print("10.py 프로세스 아이디:", os.getpid())
    child1 = Process(target=coke).start()
    time.sleep(0.5)
    child2 = Process(target=cider).start()
    time.sleep(0.5)
    child3 = Process(target=juice).start()
    time.sleep(0.5)

# 명령어: ps -el | grep python
# python이라는 이름을 포함하는 프로세스들의 상세내역(-el)을 보여줘
