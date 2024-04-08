import tracemalloc  # ptyhon 3.4이상에서 지원, 메모리가 어떻게 할당되었는지 추척하고자 할때

tracemalloc.start()
# 메모리 할당이 진행되는 작업
data = [b"%d" % i for i in range(1, 10001)]
joined_data = b" ".join(data)

current, peak = tracemalloc.get_traced_memory()  # 현재 사용량, 최대 사용량
print(f"현재 메모리 사용량: {current/ 10**6} MB")
print(f"최대 메모리 사용량: {peak/ 10**6} MB")
tracemalloc.stop()

# tracemalloc 하느라 사용한 메모리 보기
traced = tracemalloc.get_tracemalloc_memory()
print(traced / 10**6)
