# [Bronze III] 지속 - 11648 

[문제 링크](https://www.acmicpc.net/problem/11648) 

### 성능 요약

메모리: 31120 KB, 시간: 32 ms

### 분류

사칙연산, 구현, 수학

### 제출 일자

2024년 9월 8일 21:57:09

### 문제 설명

<p>키파는 곱하기를 좋아한다. 그래서 키파는 수를 보면 각 자리 숫자를 모두 곱해서 하나의 수를 만든다. 키파는 기쁘다. 키파는 이 작업을 계속해서 반복한다. 그런데 수가 한 자리가 되었다. <strong>키파는 슬퍼졌다</strong>.</p>

<p>키파의 기쁨이 지속될 수 있는 것이 몇 단계인지를 출력하는 프로그램을 작성하시오. 예를 들어 679라면:</p>

<ul>
	<li>679 → 6*7*9 = 378 (1단계)</li>
	<li>378 → 3*7*8 = 168 (2단계)</li>
	<li>168 → 1*6*8 = 48 (3단계)</li>
	<li>48 → 4*8 = 32 (4단계)</li>
	<li>32 → 3*2 = 6 (5단계: <strong>키파는 슬퍼졌다</strong>.)</li>
</ul>

<p>키파는 5단계만에 슬퍼지므로 5를 출력하면 된다.</p>

### 입력 

 <p>각각의 입력은 하나의 테스트 케이스로 이루어진다. 입력은 첫 번째 줄에 선행하는 0이 없는 9자리 이하의 수가 하나 주어진다.</p>

### 출력 

 <p>각각의 입력에 대해 키파의 기쁨이 지속될 수 있는 단계의 수를 출력하라. </p>

