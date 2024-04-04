from multiprocessing import Process
import os


def func():
    print("hello, this is test function")
    print("my process id : ", os.getpid())
    print("my parent process id : ", os.getppid())


if __name__ == "__main__":
    print("05.py 프로세스 아이디:", os.getpid())
    child = Process(target=func).start()
