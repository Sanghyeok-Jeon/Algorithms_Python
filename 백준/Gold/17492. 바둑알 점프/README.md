# [Gold IV] 바둑알 점프 - 17492 

[문제 링크](https://www.acmicpc.net/problem/17492) 

### 성능 요약

메모리: 31120 KB, 시간: 40 ms

### 분류

백트래킹, 브루트포스 알고리즘

### 제출 일자

2024년 6월 26일 09:02:30

### 문제 설명

<p>바둑알 점프는 판 위에 있는 바둑알을 하나만 남기고 모두 없애는 게임이다. 바둑알은 가로, 세로, 대각선으로 인접한 바둑알 하나를 점프하여 움직일 수 있다. 움직였을 때, 뛰어넘은 바둑알은 없어진다. 이때 뛰어넘을 바둑알이 없으면 움직일 수 없다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/f7b003c7-b0bb-4815-a8f7-6341049587b4/-/preview/"></p>

<p>예를 들어, [그림1]에서 왼쪽 상단 바둑알을 오른쪽 하단 대각선 방향으로 움직이면 [그림2] 와 같이 된다. [그림3]에서 오른쪽 하단에 있는 바둑알은 뛰어 넘을 바둑알이 없으므로 움직일 수 없다.</p>

<p>바둑알이 놓이는 판은 <em>N</em> × <em>N</em>의 정사각 행렬이고 한 칸은 1 × 1 행렬이다. 판은 빈 칸 혹은 벽으로 구성된다. 바둑알은 항상 빈 칸으로만 이동할 수 있고 벽을 뛰어넘을 수 없다. 바둑알이 없어진 칸은 빈 칸이 된다. 바둑알 점프는 바둑알 하나를 골라 점프하여 바둑알 하나를 없애고 다시 남은 바둑알들 중에 하나를 골라 점프하는 행위를 반복하여 바둑알을 1개만 남기면 승리한다.</p>

<p>판 위에 바둑알의 배치 정보가 주어진다. 바둑알 점프를 했을 때 승리할 수 있는지 판별하는 프로그램을 작성하라.</p>

### 입력 

 <p>입력의 첫 줄에 양의 정수 <em>N</em>이 주어진다. 이는 <em>N</em> × <em>N</em> 정사각 행렬의 한 변의 길이이다. 그 다음 줄부터 <em>N</em>개의 줄에 걸쳐 판의 상태가 주어진다. 각 줄은 <em>N</em>개의 정수가 공백으로 구분되어 주어지는데, 각각의 정수는 0, 1 또는 2이다. 여기서 0은 빈 칸, 1은 벽, 2는 바둑알을 의미한다.</p>

### 출력 

 <p>바둑알 점프를 하여 바둑알을 1개만 남길 수 있다면 <code>Possible</code>을, 불가능하다면 <code>Impossible</code>을 출력한다.</p>

