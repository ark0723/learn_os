import psutil, os

print("메모리 사용량 조회하기")

memory_dict = dict(psutil.virtual_memory()._asdict())  # 메모리 정보를 dict로 받겠다
print(memory_dict)

total = memory_dict["total"]  # 물리적인 메모리의 총량
available = memory_dict["available"]  # 즉시 제공가능한 양
percent = memory_dict["percent"]  # 사용중인 비율

print(f"메모리 총량 : {total}")
print(f"메모리 즉시 제공 가능량 : {available}")
print(f"메모리 사용률 : {percent}")

pid = os.getpid()
current_process = psutil.Process(pid)
# 현재 프로세스가 사용한 물리적 메모리의 양 :current_process.memory_info()[0]
kb = current_process.memory_info()[0] / 2**20  # 2**20으로 나누면 -> kb단위로 변환됨
print(f"메모리 사용량 : {kb:.2f} KB")
