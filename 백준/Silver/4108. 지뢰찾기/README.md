# [Silver V] 지뢰찾기 - 4108 

[문제 링크](https://www.acmicpc.net/problem/4108) 

### 성능 요약

메모리: 33432 KB, 시간: 548 ms

### 분류

구현

### 제출 일자

2025년 3월 20일 09:13:19

### 문제 설명

<p><iframe frameborder="0" height="360" src="https://www.youtube.com/embed/LHY8NKj3RKs" width="640"></iframe></p>

<p>07년 개봉한 영화 '지뢰찾기'는 지뢰의 수를 조사해야하는 요원 예슬의 이야기를 다룬 영화다.</p>

<p>정보기관의 요원이었던 예슬은 심심해서 컴퓨터로 지뢰찾기를 켰다가 인사팀에 걸려 지뢰제거팀으로 좌천된다. 좌천된 예슬에게 처음 부여된 임무는 지뢰 제거도 아닌 지뢰 수 조사!<br>
예슬의 첫 임무에서 교육요원으로 배정된 다민은 "처음 건 무조건 안 터져." 라고 말하며 거침없이 땅을 팠지만 지뢰가 터져 얄짤없이 사망하고 만다. 지뢰 밭에 혼자 남겨진 예슬! 과연 임무를 마치고 안전하게 돌아갈 수 있을 것인가!</p>

<p>지뢰밭은 R X C개의 칸으로 이루어져있다.</p>

<p>예슬이 발을 딛는 구역 중에서 일부 칸에는 지뢰가 들어있고 나머지는 모두 비어있다. 예슬은 모든 비어있는 칸마다 인접해 있는 지뢰의 개수를 세서 적어야 한다.</p>

<p>선이나 점을 공유하고 있는 두개의 칸을 인접해있다고 정의한다. 즉, 모든 칸은 최대 8개의 인접한 칸을 갖고 있다. (상, 하, 좌, 우, 4개의 대각선칸)</p>

### 입력 

 <p>여러 개의 테스트 케이스가 제공된다.</p>

<p>각 테스트 케이스의 첫 번째 줄에는 행과 열의 수를 표현하는 두 개의 정수 R,C가 입력된다. (1 ≤ R,C ≤ 100)</p>

<p>이후 입력되는 R개의 줄은 C개의 문자로 이루어져있다. 각 문자는 지뢰를 표현하는 '*'과 빈 공간을 표현하는 '.' 이다.</p>

<p>0 0이 입력되면 종료된다.</p>

### 출력 

 <p>C개의 문자들이 포함된 R개의 줄을 출력한다. 단, 모든 '.' 대신 인접한 칸에 위치한 지뢰의 수로 변경해 출력한다. '*' 칸은 그대로 출력한다.</p>

<p>문자 사이에 공백이나 줄 사이에 공백 줄이 있어선 안 된다.</p>

