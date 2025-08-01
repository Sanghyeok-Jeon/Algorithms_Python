# [Bronze I] 알고리즘 수업 - 선택 정렬 1 - 23881 

[문제 링크](https://www.acmicpc.net/problem/23881) 

### 성능 요약

메모리: 33432 KB, 시간: 2220 ms

### 분류

구현, 시뮬레이션, 정렬

### 제출 일자

2024년 12월 21일 13:01:50

### 문제 설명

<p>오늘도 서준이는 선택 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.</p>

<p><em>N</em>개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 선택 정렬로 배열 A를 오름차순 정렬할 경우 <em>K </em>번째 교환되는 수를 구해서 우리 서준이를 도와주자.</p>

<p>크기가 <em>N</em>인 배열에 대한 선택 정렬 의사 코드는 다음과 같다.</p>

<pre>selection_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
    for last <- N downto 2 {
        A[1..last]중 가장 큰 수 A[i]를 찾는다
        if (last != i) then A[last] <-> A[i]  # last와 i가 서로 다르면 A[last]와 A[i]를 교환
    }
}</pre>

### 입력 

 <p>첫째 줄에 배열 A의 크기 <em>N</em>(5 ≤ <em>N</em> ≤ 10,000), 교환 횟수 <em>K</em>(1 ≤ <em>K</em> ≤ N)가 주어진다.</p>

<p>다음 줄에 서로 다른 배열 A의 원소 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어진다. (1 ≤ A<sub>i</sub> ≤ 10<sup>9</sup>)</p>

### 출력 

 <p><em>K </em>번째 교환되는 두 개의 수를 작은 수부터 한 줄에 출력한다. 교환 횟수가 <em>K </em>보다 작으면 -1을 출력한다.</p>

