import psutil

# 프로세스 계층 확인( 부모 프로세스와 자식 프로세스는 서로 독립적이다)

for proc in psutil.process_iter():
    ps_name = proc.name()

    if "chrome" in ps_name.lower():
        child = proc.children()  # 자식 프로세스
        print(
            f"process : {ps_name} status : {proc.status} parent : {proc.parent} children : {child}"
        )
