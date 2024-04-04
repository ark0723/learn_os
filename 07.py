# 내 파이썬 프로그램의 이름을 알아보자
import psutil
import os


def funct():
    print("test function")


if __name__ == "__main__":
    print("07.py 프로세스 아이디:", os.getpid())
    for proc in psutil.process_iter():
        if proc.pid == os.getpid():
            print(proc.name)
