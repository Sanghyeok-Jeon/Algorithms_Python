# [Bronze IV] 엘리스 트랙 매칭 - 31428 

[문제 링크](https://www.acmicpc.net/problem/31428) 

### 성능 요약

메모리: 31120 KB, 시간: 44 ms

### 분류

구현, 문자열

### 제출 일자

2024년 4월 28일 21:09:29

### 문제 설명

<p>엘리스 트랙은 2020년부터 시작한 KDT(K-Digital Training) 교육이며 Cloud 트랙, SW 엔지니어 트랙, IOT 트랙, AI 트랙 총 4가지 트랙이 있다.</p>

<p>누적 1000명 이상의 수료생을 배출하였고, 현업에서 활동하는 많은 수료생이 존재하는 엘리스 트랙을 신청할 시 성수/부산 엘리스랩을 이용할 수 있다. 또한, 현직 개발자의 멘토링을 직접 받을 수 있는 시간이 보장되며, 모든 트랙이 2개 이상의 실무와 비슷한 프로젝트를 수행 및 발표하여 피드백을 받을 수 있다. 그 외에 개발 블로그 챌린지, 스터디, 성수낙낙 오프라인 출석챌린지, 네트워킹 세션 등이 추가로 제공된다. 교육 수료 후 6개월간 취업 지원 프로그램이 제공되며, 대표적으로는 이력서 특강, 포트폴리오 특강, 직무 특강, 기술면접 특강 등이 진행된다.</p>

<p style="text-align: center;"><img alt="" height="575" src="" width="738"></p>

<p>헬로빗은 이러한 엘리스 트랙에 매력을 느껴 친구들 $N$명을 모아 같이 엘리스 트랙에 지원하려 한다. 헬로빗의 친구들과 헬로빗이 지원하는 트랙에 대한 정보가 주어질 때, 헬로빗이 지원하는 트랙과 같은 트랙을 지원하는 헬로빗의 친구들은 총 몇 명이 있는지 출력하는 프로그램을 작성해 보자.</p>

### 입력 

 <p>첫 번째 줄에 친구들의 수를 의미하는 정수 $N$이 주어진다. $(1 \leq N \leq 10 \, 000)$</p>

<p>두 번째 줄에 헬로빗의 친구들이 지원하는 엘리스 트랙에 대한 정보 $N$개가 공백으로 구분되어 주어진다.</p>

<p>세 번째 줄에 헬로빗이 지원하는 엘리스 트랙에 대한 정보가 주어진다.</p>

<p>엘리스 트랙에 대한 정보는 Cloud 트랙은 <code>'<span style="color:#e74c3c;">C</span>'</code>, SW 엔지니어 트랙은 <code>'<span style="color:#e74c3c;">S</span>'</code>, IOT 트랙은 <code>'<span style="color:#e74c3c;">I</span>'</code>, AI 트랙은 <code>'<span style="color:#e74c3c;">A</span>'</code>로 주어진다.</p>

### 출력 

 <p>헬로빗이 지원하는 트랙과 같은 트랙을 지원하는 헬로빗의 친구들은 총 몇 명이 있는지 출력한다.</p>

