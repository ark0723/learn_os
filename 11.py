# 부모 자식간 프로세스의 통신
from multiprocessing import Process, Pipe
import os


def send(conn):
    print(f"{os.getpid()}가 {os.getppid()}에게 데이터를 보낸다!")
    conn.send("hello parent!")
    conn.close()


if __name__ == "__main__":
    parent, child = Pipe()  # 현재 프로세스, 생성하는 자식 프로세스
    p = Process(target=send, args=(child,))
    p.start()
    print("기존 프로세스 아이디:", os.getpid())
    print(parent.recv())  # send()가 반환됨
    p.join()  # 프로세스가 종료할때까지 작업을 기다린다
