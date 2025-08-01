# [Bronze III] 모험의 시작 - 31789 

[문제 링크](https://www.acmicpc.net/problem/31789) 

### 성능 요약

메모리: 31120 KB, 시간: 44 ms

### 분류

구현

### 제출 일자

2024년 5월 20일 19:29:08

### 문제 설명

<p><code>PULSE</code>를 떠나게 된 산지니 4인조는 저금통에 조금씩 모아둔 돈을 가지고 모험을 떠나기로 했다.</p>

<p>모험을 떠나기 위해서는 문지기 후안과의 대결에서 이겨야 한다. 문지기 후안을 이기려면 후안의 공격력보다 높은 무기를 가지고 있어야 한다. 그래서 4인조는 문지기 후안과 대결하기 전에 상점에서 무기를 구매하려고 한다. 4인조는 상점에서 판매하는 $N$개의 무기 중 <strong>하나만</strong>을 구매할 수 있으며 4인조가 가진 돈 $X$보다 비싼 무기는 구매할 수 없다. 산지니 4인조가 후안을 이기고 모험을 떠날 수 있을지 알아보자!</p>

### 입력 

 <p>첫 번째 줄에 상점에서 판매하는 무기의 수 $N$이 주어진다. $(1 \leq N \leq 100)$</p>

<p>두 번째 줄에 산지니 4인조가 가진 돈 $X$와 후안의 공격력 $S$가 공백으로 구분되어 주어진다. $(1 \leq X, S \leq 10^{9})$</p>

<p>세 번째 줄부터 $N + 2$번째 줄까지 $i$번째 무기의 가격 $c_i$와 공격력 $p_i$가 공백으로 구분되어 주어진다. $(1 \leq c_i, p_i \leq 10^{9})$</p>

<p>주어지는 모든 수는 정수이다.</p>

### 출력 

 <p>모험을 떠날 수 있으면 <span style="color:#e74c3c;"><code>YES</code></span>, 떠날 수 없으면 <span style="color:#e74c3c;"><code>NO</code></span>를 출력한다.</p>

