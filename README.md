# Algorithm with python

알고리즘 유형에 따라 폴더를 분류 했습니다

각 폴더별
1. 백준 문제
2. 책 '이것이 취업을 위한 코딩 테스트다' 수록 예제 및 기출 문제
<br>

# 목차
<details>
<summary>백준(BOG)</summary>
<div markdown="1">

  - 11-완전탐색(brute_force)
  - 12-정렬(sort)
  - 15-동적계획법1(dynamic_programing)
  - 16-그리디알고리즘(greedy)
  - 17-정수론&조합론
  - 21-이분탐색(binary_search)
  - 24-DFS&BFS
  - 33-동적계획법3
  - extra

  </div>
</details>

<details>
<summary>이것이취업을위한코딩테스트다</summary> <br>
<div>
  
<details>
<summary>part2-예제</summary>
<div markdown="1">

<details>
<summary>greedy</summary>
<div markdown="1">

현재 상황에서 지금 당장 좋은 것만 고르는 방법
  
그리디 알고리즘은 기준에 따라 좋은 것을 선택하는 알고리즘이므로, 
문제에서 '가장 큰 순서대로' 또는 '가장 작은 순서대로'와 같은 기준을 알게 모르게 제시한다.
>  위 예시같은 큰/작은 순서대로라는 기준은 정렬 알고리즘을 사용하면 만족시킬 수 있어, 정렬 알고리즘 문제와 자주 짝을 이루어 출제됨
  
</div>
</details>  
  
- 1-greedy
- 2-implementation
- 3-DFS&BFS
- 4-sort
- 5-binary_search
- 6-dynamic_programing
- 7-shortest_route
- 8-graph

</div>
</details>

<details>
<summary>part3-기출</summary>
<div markdown="1">

- 1-greedy
- 2-implementation
- 3-DFS&BFS
- 4-sort
- 5-binary_search
- 6-dynamic_programing
- 7-shortest_route
- 8-graph
- 9-2020_상반기_삼성전자

</div>
</details>
    
</div>
</details>

<details>
<summary>프로그래머스(추가예정)</summary>
<div markdown="1">

</div>
</details>
<br>

# 복잡도
- 시간 복잡도 : 알고리즘을 위해 필요한 연산의 횟수
- 공간 복잡도 : 알고리즘을 위해 필요한 메모리의 양

<details>
<summary>시간 복잡도</summary>
<div markdown="1">

제한시간이 1초일 때
|N 의 범위|권장 시간 복잡도|
|---|---|
|500|O(N³)|
|2,000|O(N²)|
|100,000|O(NlogN)|
|10,000,000|O(N)|
  
</div>
</details>

<details>
<summary>공간 복잡도</summary>
<div markdown="1">

일반적으로 코딩 테스트에서 제시되는 메모리 사용량을 128~512MB
- 데이터 개수가 1,000만 단위가 넘어가지 않도록 알고리즘을 설계해야한다.
> 만약 그 이상이라면, 알고리즘 설계가 잘못되었을 확률이 높다.

int 자료형 데이터의 개수에 따른 메모리 사용량
|데이터 개수|메모리 사용량|
|---|---|
|1,000|약 4KB|
|1,000,000|약 4MB|
|10,000,000|약 40MB|

Pypy3는 Pyhon3의 문법을 그대로 지원하면서, 대부분 실행속도가 더 빠르다.
즉, 같은 코드라도 Pypy3로 제출했을 때 실행속도를 더 줄일 수 있다.

만약, 반복문이 많이 필요한 알고리즘이고, 코딩테스트에서 환경에서 Pypy3를 지원한다면 이를 활용하자. 
> 삼성전자 공채의 경우 응시자가 python3로 제출한 경우 pypy3로 채점한다.
  
</div>
</details>
<br>

# 알고리즘 
<details>
<summary>greedy</summary>
<div markdown="1">

그리디 알고리즘은 '현재 상황에서 지금 당장 좋은 것만 고르는 방법'을 의미한다.

기준에 따라 좋은 것을 선택하는 알고리즘이므로, 문제에서 기준에 대한 힌트를 제시한다.
> '가장 큰 순서대로' or '가장 작은 순서대로'와 같은 크기와 순서에 대한 기준이 자주 제시되는데,
> '정렬 알고리즘'을 사용하면 해당 기준을 만족 시킬 수 있어
> '정렬 알고리즘'과 자주 짝을 이루어 출제 된다.
  
</div>
</details>
 
<details>
<summary>implementation</summary>
<div markdown="1">

- bruteforce(완전 탐색) : 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
- simulation(시뮬레이션) : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행
  
</div>
</details>  
  
<details>
<summary>DFS&BFS</summary>
<div markdown="1">

- depth_first_search(깊이 우선 탐색)
    - 깊이 우선 탐색 알고리즘이며 그래프를 탐색하는 알고리즘이다. 최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작하며 스택 자료구조를 이용한다.
    - 시간 복잡도 : O(N)
- breadth_first_search(너비 우선 탐색)
    - 가까운 노드부터 탐색하는 알고리즘이다. 선입선출 방식의 큐를 이용한다.
    - 시간 복잡도 : O(N), 일반적인 경우 실제 수행 시간은 DFS 보다 좋은 편이다.

> 인접 행렬 vs 2차원 인접 리스트   
> 인점 행렬 : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
> ```
> # 인접 행렬 예시
> graph = [[] for _ in range(3)]
> 
> # 노드 0에 연결된 노드 정보 : (노드, 거리)
> graph[0].append((1, 7))
> graph[0].append((2, 5))
> 
> # 노드 1에 연결된 노드 정보 : (노드, 거리)
> graph[1].append((0, 7))
> ```
>
> 인접 리스트 : 리스트로 그래프의 연결 관계를 표현하는 방식
> ```
> # 인접 리스트 예시
> 
> INF = 987654321  # 10e9, 연결되어있지 않음을 무한 비용으로 표현
> 
> graph = [
>       [0, 7, 5],
>       [7, 0, INF],
>       [5, INF, 0]
>   ]
> ```
> 
> 인접 행렬 방식은 모든 관계를 저장하므로, 노드 개수가 많을수록 메모리가 불필요하게 낭비된다.
>
> 인접 리스트 방식은 특정 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느리다. 
>
> 따라서, 특정한 노드와 연결된 모든 인접 노드를 순회해야 하는 경우, 
> 인접 리스트 방식이 인접 행렬 방식에 비해 메모리 공강의 낭비가 적다.

</div>
</details>  

<details>
<summary>sort</summary>
<div markdown="1">

- selection_sort(선택 정렬)
- insertion_sort(삽입 정렬)
- quick_sort(퀵 정렬)
- count_sort(계수 정렬)

</div>
</details>  

<details>
<summary>sort</summary>
<div markdown="1">

- selection_sort(선택 정렬) 
    - 시간 복잡도 : O(N²)
    - 공간 복잡도 : O(N)
    - 매번 가장 작은 것을 선택
- insertion_sort(삽입 정렬)
    - O(N²), 최선의 경우 O(N)까지 가능 > 정렬이 거의 되어 있는 경우
    - 공간 복잡도 : O(N)
    - 정렬되어 있는 데이터 리스트에서 적절한 위치를 찾은 뒤에 그 위치에 삽입
    - 필요할 때만 위치를 바꾸므로 데이터가 거의 정렬되어 있을 때 다른 알고리즘 보다 훨씬 빠르고, 효율적
- quick_sort(퀵 정렬) : 
    - 시간 복잡도 : 최악의 경우 O(N²), 평균 O(NlogN)
    - 공간 복잡도 : O(N)
    - 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.
    - 데이터가 무작위로 입력되는 경우 빠르게 동작할 확률이 높지만, 이미 데이터가 정렬되어 있는 경우 매우 느리게 동작한다.
- count_sort(계수 정렬) : 
    - 시간 복잡도 : O(N + K), (K : 데이터 중 최대값의 크기)    
    - 공간 복잡도 : O(N + K)
    - 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 잇을 때
    - 모든 범위를 담을 수 있는 크기의 리스트를 선언 후 각 크기에 따른 갯수를 저장
    - 동일한 값을 가지는 데이터가 여러 개 등장할 때 적합하다.
- radix_sort(기수정렬)
- heap_sort(힙 정렬)
- 병합 정렬 : 최악의 경우 O(NlogN)

</div>
</details>  

<details>
<summary>binary_search</summary>
<div markdown="1">

이전 탐색

</div>
</details>  

<details>
<summary>ext</summary>
<div markdown="1">

- dynamic_programing
- shortest_route
  - dijkstra(다익스트라)
  - floyd_warshall(프로이드 워셜)
- graph
  - dishoint_sets(서로소 집합)
  - kruskal(크루스칼)
  - topology_sort(위상 정렬)
  
</div>
</details>  
<br>

# 알고리즘 풀이법
<details>
<summary>세부사항</summary>
<div markdown="1">

1. 문제에 대한 이해를 적는다.
2. 입력 값을 확인한다.
   - 입력 값의 범위를 통해 짜야할 알고리즘의 최대 시간 복잡도를 체크한다. > 필요한 알고리즘에 대한 힌트를 얻을 수 있다.
   - 문제에는 나타나 있지 않는 입력 값에 대한 설명을 체크한다. ex) 입력 숫자 0 은 빈칸을 의미한다. 'end' 가 입력되면 프로그램을 종료한다.
   - 극단적인 입력값 테스트 케이스를 고려한다.
3. 출력 값을 확인한다.
   - 문제에는 나타나 있지 않은 출력 값에 대한 예외처리를 체크한다. ex) 불가능한 경우 -1 을 출력한다.
4. 필요한 변수 생성 및 입력 값 초기화
  
</div>
</details> 

# 추가 정보
백준 단계별 :  https://www.acmicpc.net/step   
blog : https://hayleykimlog.tistory.com
