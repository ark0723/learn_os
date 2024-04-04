import threading, os


def func():
    print("hello, this is test function")
    print("my process id : ", os.getpid())
    print("thread id : ", threading.get_native_id())


if __name__ == "__main__":
    print("기존 프로세스 아이디 : ", os.getpid())
    thread1 = threading.Thread(target=func).start()
    thread2 = threading.Thread(target=func).start()
    thread3 = threading.Thread(target=func).start()
