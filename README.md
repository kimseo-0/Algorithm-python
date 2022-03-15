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

# 알고리즘 
<details>
<div markdown="1">

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
- implementation
- DFS&BFS
  - depth_first_search(깊이 우선 탐색)
  - breadth_first_search(너비 우선 탐색)
- sort
  - selection_sort(선택 정렬)
  - insertion_sort(삽입 정렬)
  - quick_sort(퀵 정렬)
  - count_sort(계수 정렬)
- binary_search(이진 탐색)
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

# 추가 정보
백준 단계별 :  https://www.acmicpc.net/step   
blog : hayleykimlog.tistory.com
