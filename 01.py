# interrupt example

import time
import signal  # 비동기 인터럽트에 대한 모듈


def handler(signum: int, frame):
    # signum: 인터럽트의 유형
    print("키보드 인터럽트 검사")
    print("신호번호: ", signum)
    print("스택 프레임: ", frame)
    exit()


signal.signal(signal.SIGINT, handler)

while True:
    print("5초 간격으로 출력 중...")
    time.sleep(5)
