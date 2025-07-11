# [Bronze III] 찬반투표 - 27736 

[문제 링크](https://www.acmicpc.net/problem/27736) 

### 성능 요약

메모리: 31256 KB, 시간: 48 ms

### 분류

구현

### 제출 일자

2023년 8월 8일 23:42:31

### 문제 설명

<p>중앙대학교에서 재학생을 대상으로 하는 어떤 찬반투표가 치러졌다. 모든 재학생은 각자 찬성이나 반대, 혹은 기권 중 하나로 투표에 응답하였다.</p>

<p>해당 투표에서 찬성이 반대보다 많으면 투표가 통과된다. 반대가 찬성보다 많거나, 반대와 찬성의 수가 동일하다면 투표는 통과되지 않는다. 단, 기권한 사람이 재학생의 절반 이상이라면 찬성과 반대의 수와 관계없이 항상 투표는 무효 처리된다.</p>

<p>재학생들의 투표 내역을 입력받아 찬반투표의 결과를 출력하는 프로그램을 구현하시오.</p>

### 입력 

 <p>첫 번째 줄에 중앙대학교 재학생의 수 $N$이 주어진다.</p>

<p>두 번째 줄에 $N$개의 투표 내역이 공백으로 구분되어 주어진다. 각각 찬성은 <span style="color:#e74c3c;"><code>1</code></span>, 반대는 <span style="color:#e74c3c;"><code>-1</code></span>, 기권은 <span style="color:#e74c3c;"><code>0</code></span>으로 주어진다.</p>

### 출력 

 <p>투표가 통과되었으면 <span style="color:#e74c3c;"><code>APPROVED</code></span>, 통과되지 않았으면 <span style="color:#e74c3c;"><code>REJECTED</code></span>, 무효 처리되었으면 <span style="color:#e74c3c;"><code>INVALID</code></span>를 출력한다.</p>

