# 파일 입출력 예제

with open("number_one.txt", "w") as f:
    f.write("one")
with open("number_two.txt", "w") as f:
    f.write("two")
with open("number_three.txt", "w") as f:
    f.write("three")
with open("number_four.txt", "w") as f:
    f.write("four")

# 파일이름의 패턴을 이용해 한꺼번에 파일에 접근하기
import glob

for filename in glob.glob("*.txt", recursive=True):
    print(filename)

# 한꺼번에 여러 파일이 접근해서 내용을 변경,추가
import fileinput

with fileinput.input(glob.glob("number_*.txt")) as fi:
    for line in fi:
        print(line)

import fnmatch  # filename match
import os

# os.listdir(): ()안에 있는 디렉토리의 내용을 모두 리스트로 만든다
# '.': 현재경로
for filename in os.listdir("."):
    # regular expression: ?(아무 문자 1개), *(글자수 상관없이 모든 문자)
    if fnmatch.fnmatch(filename, "??????_one.txt"):
        print(filename)
