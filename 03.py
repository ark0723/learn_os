# pip3 install psutil
# 내 컴퓨터에서 돌아가는 프로세스 조회하기
import psutil

for proc in psutil.process_iter():
    ps_name = proc.name()  # 프로세스 이름
    if "chrome" in ps_name.lower():
        print(f"process name: {ps_name} process id: {proc.pid}")
