# operating system
- 컴퓨터에 포함된 CPU나 메모리, 입출력 기기 등이 사용자의 기대에 맞게 역할을 수행할 수 있도록 도와주는 창구 역할을 하는 시스템 소프트웨어
- 역할:
    - 프로세스 관리
    - 메모리 관리
    - 파일 시스템 관리

# Hardware
###  CPU의 구성요소
- ALU(Arithmetic and logical unit): 산술연산과 논리연산을 담당하는 회로 
- CU(Control Unit): 명령어를 해석하고 이를 실행하기 위한 제어 신호들을 순차적으로 발생시킴
- Register: 데이러를 처리하기 위한 CPU내부의 임시저장장치로 엑세스 속도가 컴퓨터의 기억장치들 중 가장 빠름

### 메인메모리 : RAM(Random Access Memory) 
- 프로그램의 실행파일이 올라가서 실행되는 영역
- 프로세스 관리


### bus system: 
- 데이터를 주고 받기 위해 사용되는 경로
- Data Bus : 데이터 이동을 위해 필요한 버스
- Control Bus : CPU가 원하는 바를 메모리에 전달하기 위한 버스
- Address Bus : 주소값을 이동하기 위해 필요한 버스


# clock pulse

# 프로그램 실행 과정
### 폰 노이만 구조

- 프로그램 코드 -> 어셈블리 코드 -> 바이너리 코드
- 컴파일러 거쳐 실행파일이 만들어짐 -> 메모리(RAM)에 올라감 -> CPU에 의해 명령어가 순차적으로 실행(1. Fetch: 메모리상의 명령어를 CPU로 가져온다(instrurctor register). 2. Decode: 가져온 명령어를 해석(CU 가 수행), 3. 실행: ALU가 수행)

### Interrupt
- CPU가 어떤 작업을 수행하고 있을때 CPU의 작업을 방해하는 신호
- 정상적으로 수행할 수 없는 명령어가 입력되면, CPU는 인터럽트를 발생시키며, 이를 예외(Exception)라고 부른다.
- 입출력장치(hardware)로부터 발생하는 인터럽트는 비동기 인터럽트라고 불리기도 함


# 프로세스
- 실행중인 프로그램을 뜻함
- 프로그램을 더블클릭하면 운영체제는 필요한 지원을 할당, 관리하기 시작

## 프로세스 구조
- 명령어가 담긴 code 영억
- 전역변수 등(static, global variables)이 담긴 data 영역
- 지역변수 등(local variable)이 담긴 stack 영역
- 동정 메모리 할당을 위한 heap 영역
- 프로그램의 실행을 위해서는 절대적으로 CPU의 레지스터가 필요함

## process control block (PCB)
- cpu는 한번에 하나의 연산만 수행할 수 있다.
- cpu는 여러개의 프로세스를 동시에 실행하지 않고, 빠르게 번갈아 가며 실행한다.
- 운영체제는 프로세스 컨트롤 블록(PCB)를 만들어 관리
- 여기에는 프로세스 식별을 위해 필요한 정보를 저장(프로세스 ID, 레이스터 데이터, 스케줄링 정보, 상태 등)

## context switching
- 다른 프로세스를 실행하기 위해 실행중인 프로세스를 저장하고 다른 프로세스 데이터로 교체하는 작업

## 프로세스 생성
- 프로그램 실행 시, 운영체제는 코드 영역과 데이터 영역을 메인메모리에 올리고 빈 스택과 빈 힙을 만들어 공간을 확보한다. 이는 부담이 되는 작업
- 새로운 프로세스 생성보다 기존 프로세스를 복사하는 것이 더 빠르다. 따라서 모든 프로세스는 최초의 프로세스로부터 복사된다. 이 과정을 fork() - 시스템함수의 일종
- 복사 후 자식프로세스는 코드영역과 데이터영역을 자신의 데이터로 덮어쓰는 작업을 진행 (exec())

## Thread
- 컨텍스트 스위칭으로 인한 부하를 줄이기 위해선 프로세스를 줄여야한다.
- 프로세스 안에서 thread를 만들어서 작업을 나누어 처리할 수 있다. 
- 동일한 프로세스 안에서 생성된 thread끼리는 코드영역, 데이터영역, 힙영역을 서로 공유한다.
- 단, thread는 스택영역(지역변수, 매개변수 저장)은 각자 하나씩 생성한다. 
- 스레드는 프로세스가 처리해야할 작업을 수행하기 위해 존재하는 것이므로, 코드 영역을 공유해 명령어에 접근할 수 있어야함
- 명령어 실행시 전역변수, 정적변수 등의 데이터에 접근해야 하므로 데이터영역과 힙 영역도 공유

## CPU의 스케줄링
- 여러개의 프로세스를 빠르게 번갈아 실행하기 위해, 각 프로세스가 동작하는 시간을 조금씩 나누어 배분한다. 
- 어떤 프로세스에(who), 얼마동안(how long) 할당할 것인가? 
- 프로세스 별로 요구하는 자원이 상이하기 때문에, 운영체제는 프로세스마다 우선순위를 부여하고 이를 기준으로 프로세스 실행
- 우선순위 높은 것들을 더 빨리, 더 자주 실행한다.
- 우선순위가 같은 프로세스들도 존재

## Queue
- 운영체제는 준비상태의 프로세스(CPU를 사용하기위해)와 대기상태의 프로세스(입출력장치를 사용하기 위해)를 관리하기 위해 큐 자료구조를 사용한다.

## 스케줄링 알고리즘
- 부하가 최소화되어야한다
- 컴퓨팅 자원을 효율적으로 사용해야 한다
- 균형잡힌 스케줄링을 해야한다
- 대기 및 응답시간이 너무 길어서는 안된다.
- 종류:
    - 선입선출(FIFO): 실행시간이 짧은 프로세스가 실행시간이 긴 프로세스 뒤에서 한참 기다리는 상황이 벌어질 수 있다
    - 최단작업우선: 실행시간 짧은 프로세스 먼저 처리, 프로세스의 실행 시간을 정확히 예측할 수 없어, 현실적이지 않음
    - 라운드 로빈: 정해진 시간 만큼만 cpu점유하고, 시간이 지나면 컨텍스트 스위칭하는 방식
    - 우선순위 스케줄링: 우선순위만 고려한 경우, 우선 순위가 낮은 프로세스가 배제되어 버리는 '기아'상태에 빠질 수 있다.

## 프로세스 간 통신(Inter-process communication)
- 메일슬롯 방식: 데이터를 받기 위해 프로세스가 우체통 역할을 하는 객체를 마려한고 이를 통해 데이터를 주고받는 방식
- 파이프 방식: 익멩 파이프 또는 네임드 파이프를 이용해 데이터를 주고 받는다. 익명 파이프는 서로 관계가 있는 프로세스 간에 통신을 할 때 사용하는 단방향 파이프고, 네임드 파이프는 프로세스 간에 양방향 통신을 할 때 사용하는 파이프다. 

## 동기화
- 공유자원: 프로세스간 통신에서 공동으로 이용하는 변수가 있는 파일, 입출력 기기 등을 일컬음
- 임계영역: 공유자원은 각 프로세스의 접근 순서에 따라 결과가 달라질 수 있는데, 프로세스가 동시에 실행할 겨우 문제가 발생할 수 있는 영역을 가리켜 임계영영역이라고 함
- 동기화 기법은 임계구역에서 발생할 수 있는 문제를 해결하기 위한 기법
    - '상호배제'라는 조건을 만족시켜야함
    - 상호배제: 하나의 프로세스가 임계구역에 들어갔다면, 다른 프로세스는 임계구역에 들어갈 수 없음을 뜻한다
    - 뮤텍스락: 임계구역의 문을 잠그고 해제하는 역할
    - 세마포어: 공유자원이 여러개 있을때도 적용 가능

## deadlock(교착상태)
- 네 가지 조건(상호배제, 비선점, 점유 및 내딕, 원형대기)를 만족할 경우에만 발생할 수 있다
- 공유자원을 두고 프로세스간에 교착상태에 이른 상태

## 식사하는 철학자 문제(The Dining-Philosophors Problem)

생각하고 먹으면서 그들의 생애를 보내는 5명의 철학자를 고려해 봅시다. 철학자들은 원형 테이블을 공유하며, 이 테이블은 각각 한 철학자에 속하는 5개의 의자로 둘러싸여 있습니다. 테이블 중앙에는 한 사발의 밥이 있고, 아래의 그림과 같이 테이블에는 다섯 개의 젓가락이 놓여 있습니다. 
철학자가 생각을 할 때는 다른 동료들과 상호 작용을 하지 않습니다. 때때로 철학자들은 배가 고파지는데 그럴 때에는 자신에게 가장 가까이 있는 두 개의 젓가락(왼쪽 젓가락을 먼저 집습니다)을 집으려고 시도합니다. 철학자는 한 번에 한 개의 젓가락만 집을 수도 있으며, 이미 옆 사람의 손에 들어간 젓가락을 집을 수는 없습니다. 배고픈 철학자가 동시에 젓가락을 두 개를 집으면, 젓가락을 놓지 않고 손에 들고 있는 채로 식사를 합니다. 그러다가 식사를 마치면, 젓가락 두 개를 모두 놓고 다시 생각에 빠집니다.

if: 모든 철학자가 동시에 배가 고프고 각 철학자가 왼쪽에 있는 젓가락을 잡는다면?

then:  더 사용 가능한 젓가락이 없기에 모든 철학자들은 영원히 누군가 포기하지 않는 이상 영원히 오른쪽 젓가락을 사용할 수 있을 때까지 기다립니다(deadlock - 교착상태에 이름)

solution: 
    1. 최대 4명의 철학자만이 테이블에 동시에 앉을 수 있다
    2. 한 철학자가 젓가락 두 개를 모두 집을 수 있을 때만 젓가락을 집도록 허용한다(이렇게 하려면 철학자는 임계 구역 안에서만 젓가락을 집어야 한다).
    3. 비대칭 해결안을 사용한다. 즉, 홀수 번호의 철학자는 먼저 왼쪽 젓가락을 집고 다음에 오른쪽 젓가락을 집는다. 반면에 짝수 번호의 철학자는 오른쪽 젓가락을 집고 다음에 왼쪽 젓가락을 집는다.
    -> 이웃한두 철학자가 동시에 식사하지 않는 것과 교착 상태가 발생하지 않는다는 것을 보장할 수 있으나, 철학자가 굶어죽는 것이 여전히 가능하다는 점에 유의해야함

# 메모리
## 메모리 계층
- 레지스터 : 휘발성
- 캐시(L1/L2) : 휘발성
- 메인 메모리(RAM) : 휘발성
- 보조 기억장치(HDD/SSD) : 비휘발성

## 메모리 할당방식
여러개의 프로세스를 메모리에 올려야한다면, 

1. 가변분할방식 : 프로세스 크기에 따라 할당
2. 고정분할방식(페이징) : 메모리를 고정된 크키로 미리 나눈후, 프로세스를 할당

## 스와핑
실행 상태의 프로세스는 메인 메모리에 올리고, 실행 상태가 아닌 프로세스들은 보조 장치에 마련된 스왑 영역에 올린 다음 프로세스의 상태 변화에 따라 두 공간 사이에서 프로세스가 이동(교환)되는 것을 가리켜 스와핑이라고 한다. 

## 외부단편화 
- 가변분할방식의 단점 중 하나 -> 메모리 조각모음(시스템에 부담을 주는 작업, 빈번하게 사용하기 어려움)

# 가상 메모리
실행할 프로세스가 메인 메모리보다 덩치가 큰 경우에 어떻게 할까? 
- 페이징기법(고정분할방식) : 메모리 공간을 일정한 크기의 페이지로 나누어 다룬다 -> 내부단편화가 발생하기도 함
    - 논리주소공간: 사용자와 프로세스가 참조하는 공간(실제메모리보다 더 큰 공간), 논리주소 공간의 조각을 페이지라고 부름
    - 물리주소공간: 실제 메모리의 공간, 물리주소공간의 조각을 프레임이라고 부름
    - 페이지테이블 엔트리
- 페이지드 세그멘테이션: 가변분할방식과 고정 분할방식을 혼합한 가상 메모리 관리 방식

## 요구 페이징
- CPU가 특정 페이지에 접근하는 명령어를 실행했을 때, 해당 페이지가 스왑 영역에 있어서 당장 실행시킬 수 없는 상태일 경우 '페이지 폴트' 예외가 발생.
- 페이지 폴트 예외가 발생하면 스와핑 작업이 먼저 진행된 후 프로세스가 실행된다.
- 요구페이징: 실행할 모든 프로세스를 메모리에 올려두는 것은 시스템에 부담이 될 수 있기때문에 당장 필요한 페이지만을 메모리에 우선 적재하는 방법

## 페이지 교체 정책
- 선입선출
- 최적 페이지 교체 : 이론적으로 존재
- LRU(Least Recently Used) : 최근 사용빈도에 따라 페이지 교체

## 스래싱(threashing)
- 이 모든 것의 근본적인 이유: 메모리 공간의 부족, 즉 프레임 부족
- 프레임이 부족하면 페이지 폴트가 자주 발생 -> 잦은 스와핑 작업으로 CPU사용률이 떨어지게 됨
- CPU사용률이 떨어지면 운영체제는 더 많은 프로세스를 메모리에 올리려고 하고, 더 잦은 페이지 폴트로 이어져 악순환에 빠지게 됨: 이를 스래싱이라고 함
- 프로세스의 처리시간보다 페이지 교체시간이 더 많아지는 현상
- 다중 프로그래밍의 정도가 높아짐에 따라 CPU의 이용률은 어느 특정 시점 까지는 올라가지만 다중 프로그래밍의 정도가 더욱 커지면 스레싱이 나타나고, CPU의 이용률은 급격히 감소된다.

## CPU이용률을 높이고, 스래싱 현상을 방지하는 방법
- 다중 프로그래밍의 정도를 적정 수준으로 유지한다.
- 페이지 부재율을 조절한다.
- 워킹 셋을 유지한다.
- 프로세스가 필요로 하는 만큼의 프레임을 제공한다
- 부족한 자원을 증설한다.
- 일부 프로세스를 종료한다.

## working set :워킹셋
- 프로세스가 일정 시간 동안 자주 참조하는 페이지들의 집합
- 프로그램의 Locality 특징을 이용한다
- 자주 참조되는 워킹 셋을 메인메모리(RAM)에 상주시킴으로써 페이지폴트 및 페이지 교체 현상을 줄인다
- 시간이 지남에 따라 자주 참조하는 페이지들의 집합이 변화하기 때문에 워킹 셋은 시간에 따라 바뀌게 된다

## 페이지 부재(page fault)
- 프로세스 실행 시 참조할 페이지가 메인메모리에 없는 현상
- 페이지 부재율(Page Fault Rate)에 따라 주기억장치에 있는 페이지 프레임의 수를 늘리거나 줄여 페이지 부재율을 적정 수준으로 유지하는 방식

## 파일시스템
- 하나의 파일은 여러개의 블록으로 이루어져 있다.
- 블록을 메모리에 할당할 때는 연속방식 또는 불연속 방식을 사용할 수 있다.
