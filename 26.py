# 파일 경로를 문자열이 아닌 객체로 다루기
import os
import pathlib

# pathlib.Path.cwd() : 현재 워킹디렉토리 반환
for p in pathlib.Path.cwd().glob("*.txt"):
    print(p)
    print(p.parent)  # *.txt의 부모 디렉토리 출력
    new_p = os.path.join(p.parent, p.name)
    print(new_p)
    print("=" * 50)
