# os 파일 시스템 관련 함수
import os

pwd = "/Users/mac/Desktop/learn_os"
filenames = os.listdir(pwd)
print(filenames)

# 디렉토리인지 아닌지 여부를 확인
print(os.path.isdir(filenames[0]))
print(os.path.isdir(pwd + "/anonymous"))

# 파일인지 아닌지 확인
print(os.path.isfile(filenames[0]))
print(os.path.isfile(pwd + "/anonymous"))

# 파일이름과 확장자 분리
filepath = pwd + "/" + filenames[0]
name, ext = os.path.splitext(filepath)
print(name)
print(ext)


# 경로와 확장자 이용해 파일을 찾고, 내용 읽어오기
def searchFile(dirname, extension):
    # 해당 경로에 있는 모든 파일과 폴더를 가져온다
    filenames = os.listdir(dirname)
    for f in filenames:
        filepath = os.path.join(dirname, f)
        if os.path.isdir(filepath):  # 디렉토리이면 하위 디렉토리도 검색
            searchFile(filepath, extension)  # 재귀함수
        elif os.path.isfile(filepath):  # 파일이면
            name, ext = os.path.splitext(filepath)
            if ext == extension:
                with open(filepath, "r", encoding="utf-8") as f:
                    print(f.read())


searchFile("/Users/mac/Desktop/learn_os", ".txt")

# 파일 복사 또는 이동

import shutil

pwd = "/Users/mac/Desktop/learn_os"
filenames = os.listdir(pwd)

for filename in filenames:
    if "new" in filename:
        origin = os.path.join(pwd, filename)
        print(origin)
        # 복사: shutil.copy(원본, 복사본 만들 위치)
        shutil.copy(origin, os.path.join(pwd, "copy.txt"))
        # 파일이동
        shutil.move(origin, os.path.join(pwd, "anonymous"))
